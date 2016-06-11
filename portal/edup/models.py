from __future__ import unicode_literals

from django.db import models


class school(models.Model):
    sname = models.CharField(max_length=200)
    slocation = models.CharField(max_length=200)
    sratings = models.IntegerField()
    stype = models.CharField(max_length=200)
    sweb = models.CharField(max_length=50)
# Create your models here.
