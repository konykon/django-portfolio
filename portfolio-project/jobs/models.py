from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    gitlink = models.URLField(max_length=200, null=True)
    weblink = models.URLField(max_length=200, null=True)