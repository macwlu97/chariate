from django.db import models

class AbstractDictModel(models.Model):
    '''
        Class contains common fields for all dictionaries that are in Dictionaries file
    '''

    name = models.TextField(max_length=200, null=False, unique=True)
    sh_name = models.CharField(max_length=20, null=False, unique=False)
    value = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        app_label = 'apps'
