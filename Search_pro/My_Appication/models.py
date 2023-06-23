from django.db import models

# Create your models here.
class information(models.Model):
    Name=models.CharField(max_length=20, default="")
    Phno=models.IntegerField(default="")
    Email=models.CharField(max_length=50,default="")