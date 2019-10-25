from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel

class Review(AbstractBaseModel):
    '''
        Model stores review data.
    '''
    rating = models.IntegerField()
    content = models.CharField(max_length=200, null=True, unique=False)
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

    class Meta:
        abstract = False
