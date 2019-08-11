from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class File(models.Model):
    upload_date = models.DateField(default=timezone.now)
    file_name = models.CharField(max_length=200, blank=False)
    file_upload = models.FileField(blank=False, upload_to="uploads")
    file_size_display = models.CharField(max_length=20, blank=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.file_name
