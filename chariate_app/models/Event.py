from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel

class Event(AbstractBaseModel):
    '''
        Model stores event data.
    '''
    title = models.CharField(max_length=100, null=False, unique=False)
    organization_id = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        db_column='organization_id',
        blank=True,
        null=True,
        related_name='%(class)s_organization',
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    city_id = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        db_column='city_id',
        blank=True,
        null=True,
        related_name='%(class)s_city',
    )
    logo = models.BinaryField(null=True, blank=True)
    file_type = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = False
