# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-09 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170907_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='', upload_to='static/img'),
        ),
    ]
