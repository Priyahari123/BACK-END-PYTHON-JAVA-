from django.db import models

# Create your models here.
class Addprofile(models.Model):
    Name = models.CharField(max_length=20)  
    email_id = models.CharField(max_length=30) 
    password = models.CharField(max_length=40) 
    password1 = models.CharField(max_length=30) 