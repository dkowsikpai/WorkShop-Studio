from django.db import models

# Create your models here.


class WorkShopCode (models.Model):
    heading = models.CharField(blank=False, max_length=200, default="NULL")
    text = models.TextField(blank=True, max_length=2000000)
    share = models.BooleanField(default=False)

    def __str__(self):
        return "Code"
