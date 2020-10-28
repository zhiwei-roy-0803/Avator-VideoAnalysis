# Other imports
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Module imports
from .models import Video
from .utils import *
from .processing import *


@login_required
def index(request, username):
    '''
    Render the home page for a specific user
    :param request:
    :param username:
    :return:
    '''
    try:
        videos = Video.objects.filter(owner=username)
        # 去数据库中查询这个用户拥有的所有视频的meta并返回用于更新用户主页
        items = get_all_video_meta(videos)
    except:
        items = []
    request.session.is_login = True
    request.session.user_name = username
    return render(request, 'VideoProcessing/index.html', {'items': items})

@login_required
@parser_classes((FileUploadParser, MultiPartParser, FormParser,))
def upload(request, username=''):
    '''
    Handling the video uploaded. Create a Video model instance and store it into the database (SQLite3)
    :param request:
    :param username:
    :return:
    '''
    files = request.FILES.getlist('file', None)
    if files is not None:
        # 如果上传的文件列表非空，那么遍历列表中的每一个文件，创建数据库对象并保存到本地的磁盘
        for file_obj in files:
            created_time = get_time()
            filename = file_obj.name
            video = Video()
            video.video_file = file_obj
            video.name = filename.split(".")[0]
            video.owner = username
            video.created = created_time
            video.save()
    return redirect("video:home", username=username)

@login_required
def show_original(request, username='', filename=''):
    '''
    Display the user uploaded video
    :param request:
    :param username:
    :param filename:
    :return:
    '''
    filter_dict = {"owner": username, "name": filename}
    video = Video.objects.filter(**filter_dict)[0]
    return render(request, template_name="VideoProcessing/OriginalVideoIIllustration.html", context={"vid": video})


@login_required
def show_processed(request, username='', filename=''):
    '''
    Display the processed video
    :param request:
    :param username:
    :param filename:
    :return:
    '''
    filter_dict = {"owner": username, "name": filename}
    video = Video.objects.filter(**filter_dict)[0]
    return render(request, template_name="VideoProcessing/ProcessedVideoIIllustration.html", context={"vid": video})


@login_required
def run(request, username='', filename=''):
    '''
    Perform video processing and after that, redirect to the home page of the user
    :param request:
    :param username:
    :param filename:
    :return:
    '''
    filter_dict = {"owner": username, "name": filename}
    video = Video.objects.filter(**filter_dict)[0]
    process(video)
    video.processed_video_path = os.path.join(settings.MEDIA_URL, "videos", "processed", "_".join([video.owner, video.name]) + ".mp4")
    video.save()
    return redirect("video:home", username=username)


@login_required
def destroy(request, username='', filename=''):
    '''
    Delete a Video instance in the database and delete its related video and audio files simultaneously
    :param request:
    :param username:
    :param filename:
    :return:
    '''
    filter_dict = {"owner": username, "name": filename}
    video_to_delete = Video.objects.filter(**filter_dict)[0]
    video_name = video_to_delete.name
    video_owner = video_to_delete.owner
    if video_to_delete.processed:
        related_audio_path = os.path.join(settings.MEDIA_ROOT, "audios", "_".join([video_owner, video_name]) + ".mp3")
        related_video_path = os.path.join(settings.MEDIA_ROOT, "videos", "processed", "_".join([video_owner, video_name]) + ".mp4")
        try:
            os.remove(related_audio_path)
            os.remove(related_video_path)
        except:
            print("Fail to remove related video and audio!")
    Video.objects.filter(**filter_dict).delete()
    return redirect("video:home", username=username)