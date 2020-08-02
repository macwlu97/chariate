from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel


class Like(AbstractBaseModel):
    '''
        Model stores like data.
    '''
    review_id = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        db_column='review_id',
        blank=True,
        null=True,
        related_name='%(class)s_review',
    )
    organization_id = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        db_column='organization_id',
        blank=True,
        null=True,
        related_name='%(class)s_organization',
    )
    event_id = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        db_column='event_id',
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
