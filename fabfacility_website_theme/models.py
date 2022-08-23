from pyexpat import model
from django.db import models
from django.utils import timezone


class SubscriptionEmail(models.Model):
    
    email = models.CharField(max_length=70)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.email)


class Gallery(models.Model):

    project_name = models.CharField(max_length=255)
    project_location = models.CharField(max_length=255)
    project_pic = models.ImageField(upload_to='ProjectPictures')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.project_name}"
