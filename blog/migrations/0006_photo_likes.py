# Generated by Django 3.2.20 on 2023-08-28 11:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_alter_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='photo_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
