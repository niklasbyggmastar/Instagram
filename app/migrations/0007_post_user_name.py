# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
