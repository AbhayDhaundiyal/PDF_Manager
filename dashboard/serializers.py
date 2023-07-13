from rest_framework import serializers
from dashboard.models import FileShared, File, FileDetails


class FileDetailsSerializer(serializers.ModelSerialize):
    class Meta:
        model = FileDetails
        fields = "__all__"

class FileSharedSerializer(serializers.ModelSerialize):
    class Meta:
        model = FileShared
        fields = "__all__"

class FileSerializer(serializers.ModelSerialize):
    
    class Meta:
        model = File
        fields = "__all__"