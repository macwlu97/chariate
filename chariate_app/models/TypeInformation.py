from __future__ import unicode_literals

from django.db import models

class TypeInformation(models.Model):
    '''
        Model stores information data.
    '''
    name = models.CharField(max_length=100, null=False, unique=True)
    max_use = models.IntegerField(null=True, default=1)
    text_field = models.CharField(max_length=100, null=False)


    class Meta:
        abstract = False
