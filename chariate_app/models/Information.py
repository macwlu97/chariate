from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel

class Information(AbstractBaseModel):
    '''
        Model stores information data.
    '''
    type = models.CharField(max_length=100, null=False, unique=True)
    content = models.CharField(max_length=200, null=False, unique=True)
    organization_id = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        db_column='organization_id',
        blank=True,
        null=True,
        related_name='%(class)s_organization',
    )

    class Meta:
        abstract = False
