from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel

class Organization(AbstractBaseModel):
    '''
        Model stores organization data.
    '''
    name = models.CharField(max_length=100, null=False, unique=True)
    sh_name = models.CharField(max_length=20, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    delete_date = models.DateField(null=True, blank=True)
    type = models.IntegerField(default=0)
    logo = models.BinaryField(null=True, blank=True)

    class Meta:
        abstract = False


