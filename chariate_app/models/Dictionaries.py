from chariate_app.models.AbstractModels.AbstractDictModel import AbstractDictModel
from django.db import models


class DictDecision(AbstractDictModel):
    '''
        Model is dictionary of decisions.
    '''
    class Meta:
        abstract = False

