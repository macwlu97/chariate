from __future__ import unicode_literals

from django.db import models

class City(models.Model):
    '''
        Model stores information data.
    '''
    name = models.CharField(max_length=100, null=False, unique=True)
    logo = models.BinaryField(null=True, blank=True)
    file_type = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = False
