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

    class Meta:
        abstract = False
