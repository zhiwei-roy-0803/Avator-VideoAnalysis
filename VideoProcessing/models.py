from django.db import models
from django.db import transaction
from django.conf import settings
import os.path as osp
import os

# Create your models here.

def try_remove(file_path):
    try:
        os.remove(file_path)
    except:
        pass

# Create your models here.
class Video(models.Model):
    # Created time
    created = models.DateTimeField(auto_now_add=True, null=True)
    # Unique label for the video
    name = models.CharField(max_length=100, blank=False, null=False, default='')
    # Video file
    video_file = models.FileField(upload_to="videos/uploaded", blank=True, null=True)
    # Audio path
    audio_path = models.CharField(max_length=100, blank=False, null=False, default='')
    # Processed video path
    processed_video_path = models.CharField(max_length=100, blank=False, null=False, default='')
    # Owner (Django default user model)
    owner = models.CharField(max_length=100, blank=False, null=False, default='')
    # If processed
    processed = models.BooleanField(default=False)
    # If processing is in progress
    being_processed = models.BooleanField(default=False)

    def as_dict(self):
        if self.processed:
            status = "Processed"
        else:
            status = "Wait for Processing"
        return {
            "filename": self.name,
            "is_processed": status,
            "create time": self.created
        }


