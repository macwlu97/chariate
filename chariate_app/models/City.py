from __future__ import unicode_literals

from django.db import models

class City(models.Model):
    '''
        Model stores information data.
    '''
    name = models.CharField(max_length=100, null=False, unique=True)


    class Meta:
        abstract = False
