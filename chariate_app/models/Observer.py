from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel


class Observer(AbstractBaseModel):
    '''
        Model stores observer data.
    '''
    event_id = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        db_column='event_id',
        blank=True,
        null=True,
        related_name='%(class)s_event',
    )
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
