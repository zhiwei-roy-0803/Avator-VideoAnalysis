import json
import os.path as osp
import os
import subprocess
import cv2
import tqdm
from django.conf import settings
from .rpc_client import RpcClient
from .utils import get_frame_with_bbox_face, get_frame_with_bbox_yolo3
from config import RPC_SERVICE_HOST, RPC_SERVICE_PORT

def audio_process(video_path, audio_path):
    '''
    Do some audio processing task. Currently, it just extracts raw audio signal from a video
    :param video_path:
    :param audio_path:
    :return:
    '''
    command = "ffmpeg -y -i %s -ab 160k -ac 2 -ar 44100 -vn %s" % (video_path, audio_path)
    # Extract audio from video file through ffmpeg
    print("Extracting audio content from video...")
    subprocess.call(command, shell=True)
    return audio_path


def visual_process(video_name, video_path):
    '''
    Perform object detection and face detection. All computational intensive work is accomplished in the model server
    and this func just decodes frames from video stream
    :param video_name:
    :param video_path:
    :return:
    '''
    # Use OpenCV to open a video streaming
    video_stream = cv2.VideoCapture(video_path)
    # Video meta extraction
    height = int(video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(video_stream.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(video_stream.get(cv2.CAP_PROP_FPS))
    frame_cnt = int(video_stream.get(cv2.CAP_PROP_FRAME_COUNT))
    # Intermediate (silent) video output path
    output_path = osp.join(settings.MEDIA_ROOT, "videos", "processed")
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    outfile_path = "{:s}_temp.mp4".format(osp.join(output_path, video_name.split(".")[0]))
    out = cv2.VideoWriter(
        outfile_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height),
    )
    # Process video stream in a frame-by-frame fashion. Send each frame to the model server via RPC communications
    print("Processing frames through rpc call...")
    with tqdm.tqdm(total=frame_cnt, unit="frames") as pbar:
        with RpcClient(host=RPC_SERVICE_HOST, port=RPC_SERVICE_PORT) as rpc_client:
            while True:
                # Extract single frame from the video stream
                ret, frame = video_stream.read()
                if ret == False:
                    break
                _, frame_encoded = cv2.imencode('.jpg', frame)
                json_string = rpc_client.service_request(buf=frame_encoded.tobytes())
                det = json.loads(json_string)
                frame_with_bbox = get_frame_with_bbox_yolo3(frame, det['yolo'])
                frame_with_bbox = get_frame_with_bbox_face(frame_with_bbox, det['face'])
                out.write(frame_with_bbox)
                pbar.update(1)
    # close the opened stream
    video_stream.release()
    out.release()
    return outfile_path

def postproc(tmp_video_path, audio_path, res_video_path):
    '''
    Do some post processing work. Currently, it just combine the audio signal extracted from the original video with
    the processed silent video
    :param tmp_video_path: path of intermediate video
    :param audio_path: path of raw audio
    :param res_video_path: path of the result video
    :return:
    '''
    cmd = "ffmpeg -y -i {:s} -i {:s} -c:v libx264 -c:a aac {:s}".format(
        tmp_video_path,
        audio_path,
        res_video_path
    )
    print("Combine audio extracted from original video and the processed video...")
    subprocess.call(cmd, shell=True)




# Process the video
def process(video):
    """
    :param
        video: The video object that represents a model instance
    :return:
        res: Json object that contains the prediction results for both visual and audio processing
    """
    video.being_processed = True
    video.save()
    try:
        res = dict()
        # Get absolute video path
        video_path = osp.join(settings.MEDIA_ROOT, str(video.video_file))
        audio_path = osp.join(settings.MEDIA_ROOT, "audios")
        if not os.path.isdir(audio_path):
            os.makedirs(audio_path)
        # Extract audio content
        audio_path = audio_process(video_path, audio_path=osp.join(audio_path, '_'.join([video.owner, video.name.split(".")[0] + ".mp3"])))
        # Process visual content
        tmp_video_path = visual_process(video.name, video_path)
        # Mark video as processed and save
        video.processed = True
        video.being_processed = False
        # Start postprocess
        res_video_path = osp.join(settings.MEDIA_ROOT, "videos", "processed", "_".join([video.owner, video.name]) + ".mp4")
        postproc(tmp_video_path, audio_path, res_video_path)
        # Save processed video
        video.save()
        # Once finish the combination, remove the intermediate video without audio
        try:
            os.remove(tmp_video_path)
        except:
            print("Fail to remove intermediate silent video")
        return res
    # Capture any exception and return None
    except Exception as e:
        video.being_processed = False
        video.save()
        print(e)
        return None