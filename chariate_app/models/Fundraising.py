from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel

class Fundraising(AbstractBaseModel):
    '''
        Model stores fundraising data.
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
    owner_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True,
        related_name='%(class)s_user',
    )
    description = models.TextField(blank=True, null=True)
    logo = models.BinaryField(null=True, blank=True)

    class Meta:
        abstract = False
