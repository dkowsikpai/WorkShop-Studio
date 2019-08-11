from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(WorkShopCode)
class WorkShopCodeDB(admin.ModelAdmin):
    list_display = ['heading', 'text', 'share']
