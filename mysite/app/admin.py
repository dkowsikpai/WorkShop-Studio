from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(File)
class FileUploadList(admin.ModelAdmin):
    list_display = ['file_name', 'file_upload', 'file_size_display', 'display']
