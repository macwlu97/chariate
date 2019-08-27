from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User, Organization


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class OrganizationSerializer(ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'
