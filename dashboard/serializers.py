from rest_framework import serializers
from dashboard.models import FileShared, File, FileDetails, Comments


class FileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileDetails
        fields = "__all__"

class FileSharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileShared
        fields = "__all__"

class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = File
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"