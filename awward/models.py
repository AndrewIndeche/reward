from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
Class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.ImageField(upload_to = 'images/',default='alaska.jpg')
    name = models.CharField(blank=True,max_length=60)
    bio = models.TextField(blank=True,max_length=500)

Class Post (models.Model):
Class Rate (models.Model):
