from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from chariate_app.models import User, Organization, MemberOrganization, Album, City, CityOrganization, DictDecision, \
    Event, Information, Like, Observer, Participant, Photo, Review, Fundraising, TypeInformation


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class OrganizationSerializer(ModelSerializer):

    city = serializers.SerializerMethodField(default=0)


    class Meta:
        model = Organization
        fields = '__all__'

    def get_city(self, obj):  # "get_" + field name
        try:
            all_city_org = CityOrganization.objects.all().filter(Organization_id=obj.id)
        except CityOrganization.DoesNotExist:
            return None

        if all_city_org:
            final_list = []
            for city_org in all_city_org:
                dict = {
                    "id": city_org.City.pk,
                    "name": city_org.City.name
                }
                final_list.append(dict)
            return final_list
        else:
            return None

class OrganizationPutSerializer(ModelSerializer):

    class Meta:
        model = Organization
        # fields = '__all__'
        exclude = ('name', 'sh_name')

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

class TypeInformationSerializer(ModelSerializer):

    class Meta:
        model = TypeInformation
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

class FundraisingSerializer(ModelSerializer):

    class Meta:
        model = Fundraising
        fields = '__all__'
