from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
Class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.ImageField(upload_to = 'images/',default='alaska.jpg')
    name = models.CharField(blank=True,max_length=60)
    bio = models.TextField(blank=True,max_length=500)
    location = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def delete_profile(self):
        self.delete()


Class Post (models.Model):
     title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    photo = ImageField(manual_crop='1280x720')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()


Class Rate (models.Model):
