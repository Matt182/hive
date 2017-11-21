# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20171121_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(upload_to=user_profile.models.user_directory_path),
        ),
    ]