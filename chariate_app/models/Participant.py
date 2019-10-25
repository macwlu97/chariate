from __future__ import unicode_literals

from django.db import models
from chariate_app.models import User, Event
from chariate_app.models.AbstractModels import AbstractBaseModel


class Participant(models.Model):
    '''
        Model stores participant data.
    '''
    add_date = models.DateTimeField(auto_now_add=True)
    decision = models.ForeignKey(
        'DictDecision',
        models.DO_NOTHING,
        db_column='decision_id',
        blank=True,
        null=True,
        related_name='%(class)s_decision_id'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


    class Meta:
        abstract = False
