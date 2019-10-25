from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel

class Photo(AbstractBaseModel):
    '''
        Model stores photo data.
    '''
    blob_photo = models.BinaryField()
    album_id = models.ForeignKey(
        'Album',
        on_delete=models.CASCADE,
        db_column='album_id',
        blank=True,
        null=True,
        related_name='%(class)s_album',
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
