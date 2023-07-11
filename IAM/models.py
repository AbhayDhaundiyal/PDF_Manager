from django.db import models
from django.core import validators

class User(models.Model):
    first_name = models.CharField(max_length= 20, null= False)
    last_name = models.CharField(max_length= 20, null= False)
    email = models.EmailField((""), max_length=254, null= False, unique= True, validators=[validators.EmailValidator(message="Invalid Email")])
    password = models.CharField(max_length= 30, null = False)