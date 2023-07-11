from django.db import models


class File(models.Model):
    file_name = models.CharField(max_length= 30)
    file = models.BinaryField(default= None)

class File_Shared(models.Model):
    file_id = models.BigIntegerField(null = True)
    user_id = models.BigIntegerField(null= True)
    public = models.BooleanField(default= False)
    

class Comments(models.Model):
    file_id = models.BigIntegerField(default= -1)
    User = models.BigIntegerField(default= -1)
    content = models.CharField(max_length= 300)
    parent = models.BigIntegerField(default= None)