# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edup', '0006_auto_20160611_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='simage',
        ),
        migrations.AddField(
            model_name='school',
            name='stype',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='sweb',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
