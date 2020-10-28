from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User

class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Video
        fields = "__all__"