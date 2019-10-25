from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from chariate_app.models import User, Organization, MemberOrganization, Album, City, CityOrganization, DictDecision, Event, Information, Like, Observer, Participant, Photo, Review


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


class MemberOrganizationSerializer(ModelSerializer):

    class Meta:
        model = MemberOrganization
        fields = '__all__'


class AlbumSerializer(ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class CityOrganizationSerializer(ModelSerializer):

    class Meta:
        model = CityOrganization
        fields = '__all__'


class DictDecisionSerializer(ModelSerializer):

    class Meta:
        model = DictDecision
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class InformationSerializer(ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'


class LikeSerializer(ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class ObserverSerializer(ModelSerializer):

    class Meta:
        model = Observer
        fields = '__all__'


class ParticipantSerializer(ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'


class PhotoSerializer(ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
