# Generated by Django 2.2.3 on 2019-08-07 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_file_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='upload_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
