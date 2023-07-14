from django.db import models
from datetime import datetime

class File(models.Model):
    file_id = models.BigIntegerField(null= False, default= -1)
    file = models.BinaryField(default= None)


class FileDetails(models.Model):
    file_id = models.AutoField(primary_key= True)
    file_name = models.CharField(max_length= 50)
    is_public = models.BooleanField(default= False)
    owner = models.IntegerField(default= 1)
    created_at = models.DateTimeField(default = datetime.now())


class FileShared(models.Model):
    file_id = models.BigIntegerField(null = True)
    user_id = models.BigIntegerField(null= True)


class Comments(models.Model):
    file_id = models.BigIntegerField(default= -1)
    author = models.IntegerField(default= -1)
    content = models.CharField(max_length= 300)
    parent = models.BigIntegerField(default= None, null= True)
    created_at = models.DateTimeField(default = datetime.now())