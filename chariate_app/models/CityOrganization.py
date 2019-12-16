from __future__ import unicode_literals

from django.db import models

from chariate_app.models import City, Organization
from chariate_app.models.AbstractModels import AbstractBaseModel


class CityOrganization(AbstractBaseModel):
    City = models.ForeignKey('City', related_name='city_organization', on_delete=models.CASCADE)
    Organization = models.ForeignKey('Organization', related_name='city_organization', on_delete=models.CASCADE)

    class Meta:
        abstract = False
