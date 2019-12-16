from __future__ import unicode_literals

from django.db import models

from chariate_app.models.AbstractModels import AbstractBaseModel
from chariate_app.models import CityOrganization

class Organization(AbstractBaseModel):
    '''
        Model stores organization data.
    '''
    name = models.CharField(max_length=100, null=False, unique=True)
    sh_name = models.CharField(max_length=20, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    delete_date = models.DateField(null=True, blank=True)

    # @property
    # def my_fields(self):
    #     # try:
    #     #     city_org_id = CityOrganization.objects.all() # .filter(Organization_id=self.pk).get().City.id
    #     #     return city_org_id
    #     # except CityOrganization.DoesNotExist:
    #     #     return {
    #     #     'awe': "ss",
    #     # }
    #     return {
    #         'awe': CityOrganization.objects.all().get(1).pk,
    #     }

        #dalo efekt myfield: { 'awe': "ss" }

    class Meta:
        abstract = False


