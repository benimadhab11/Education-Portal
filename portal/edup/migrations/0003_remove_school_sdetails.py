# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edup', '0002_school_sratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='sdetails',
        ),
    ]
