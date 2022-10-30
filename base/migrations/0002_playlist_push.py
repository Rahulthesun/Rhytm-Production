# Generated by Django 4.1.2 on 2022-10-28 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='push',
            field=models.ManyToManyField(blank=True, related_name='push', to=settings.AUTH_USER_MODEL),
        ),
    ]