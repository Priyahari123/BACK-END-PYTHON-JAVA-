from django.db import models

# Create your models here.
class info(models.Model):
    username=models.CharField(max_length=20, default="")
    email=models.CharField(max_length=50, default="")
    password=models.CharField(max_length=15,default="")
    re_password=models.CharField(max_length=15,default="")
    address=models.CharField(max_length=30,default="")
