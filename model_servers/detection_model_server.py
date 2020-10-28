import os, sys
sys.path.append(os.path.pardir)
import json
import time
from concurrent import futures
import cv2
import grpc
import numpy as np
import torch
from proto import api2msl_pb2, api2msl_pb2_grpc
from models.Yolo3 import Darknet
import face_recognition
# Time constant
_ONE_DAY_IN_SECONDS = 24 * 60 * 60
# Some hyper-parameter used in Yolo v3 model
conf_thres = 0.8
nms_thres = 0.4
batch_size = 1
img_size = 416


def load_yolo3():
    # Path for model configuration and pre-trained weight for YOLO model
    model_def = "../config/yolov3.cfg"
    weights_path = os.path.join(os.path.pardir, "models", "weights", "yolov3.weights")
    class_path = "../config/coco.names"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = Darknet(model_def, img_size=img_size, conf_thres=conf_thres, nms_thres=nms_thres, class_path=class_path).to(device)
    if weights_path.endswith(".weights"):
        model.load_darknet_weights(weights_path)
    else:
        model.load_state_dict(torch.load(weights_path))
    return model

# Execute face detection with face_recognition library
def face_detection(img):
    face_locations = face_recognition.face_locations(img)
    return face_locations

# Custom request service
class Api2MslServicer(api2msl_pb2_grpc.Api2MslServicer):
    def __init__(self):
        super().__init__()
        self.yolo_detector = load_yolo3()
        self.face_detector = face_detection

    def GetJson(self, request, context):
        '''
        Provide gRPC service
        :param request: request.buf-encoded jpg bytes stream
        :param context:
        :return:
        '''
        print("Start Serving Incoming Request")
        # request.buf里面是经过jpg编码之后的一帧图像
        img = cv2.imdecode(np.fromstring(request.buf, dtype=np.uint8), -1)
        det = {}
        # Run object detection with Yolo v3
        print("Run Yolo Detector")
        det["yolo"] = self.yolo_detector.detect(img) # return a dict that contains detection result
        print("Run Face Detector")
        det["face"] = self.face_detector(img)
        print("Processing Done!")
        return api2msl_pb2.JsonReply(json=json.dumps(det))


def main():
    # gRPC server configurations
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    api2msl_pb2_grpc.add_Api2MslServicer_to_server(Api2MslServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Visual Model Server Listening on port 50051")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("Shutting down visual model server")
        server.stop(0)


if __name__ == '__main__':
    main()
