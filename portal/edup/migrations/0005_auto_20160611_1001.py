# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edup', '0004_school_simage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='simage',
            field=models.ImageField(upload_to='static/searchicon.png'),
        ),
    ]
