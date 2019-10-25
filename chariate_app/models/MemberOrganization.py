from __future__ import unicode_literals

from django.db import models

from chariate_app.models import User, Organization
from chariate_app.models.AbstractModels import AbstractBaseModel


class MemberOrganization(models.Model):
    user = models.ForeignKey(User, related_name='organization_user', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='organization_user', on_delete=models.CASCADE)

    class Meta:
        abstract = False
