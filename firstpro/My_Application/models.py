from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=20, default="")
    email=models.CharField(max_length=50, default="")
    address=models.CharField(max_length=30,default="")
