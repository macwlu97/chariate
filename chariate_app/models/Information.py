from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel

class Information(AbstractBaseModel):
    '''
        Model stores information data.
    '''
    # type = models.CharField(max_length=100, null=False, unique=True)
    type_info_id = models.ForeignKey(
        'TypeInformation',
        on_delete=models.CASCADE,
        db_column='type_info_id',
        blank=True,
        null=False,
        related_name='%(class)s_typeinformation',
    )
    content = models.CharField(max_length=1000, null=False)
    organization_id = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        db_column='organization_id',
        blank=True,
        null=True,
        related_name='%(class)s_organization',
    )
    fundraising_id = models.ForeignKey(
        'Fundraising',
        on_delete=models.CASCADE,
        db_column='fundraising_id',
        blank=True,
        null=True,
        related_name='%(class)s_fundraising',
    )
    event_id = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        db_column='event_id',
        blank=True,
        null=True,
        related_name='%(class)s_event',
    )

    class Meta:
        abstract = False
