from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Organization, CityOrganization
from chariate_app.serializers import OrganizationSerializer


class SearchAPIView(APIView):
    '''
        API for handling search result.
    '''

class SearchAPIListView(APIView):
    '''
        API for handling lists of search result methods.
    '''

    def get(self, request, city_id, format=None):
        '''
            Method returns search results.
        '''
        search_text = request.GET.get('q')

        items = Organization.objects.filter(name__contains=search_text)
        result = []

        if int(city_id) is not 0:
            for item in items:
                try:
                    city_org_all = CityOrganization.objects.all().filter(Organization_id=item.id)
                except CityOrganization.DoesNotExist:
                    city_org_id = 0

                id_from_city_org_all = []
                if city_org_all:
                    for city_org_id in city_org_all:
                        id_from_city_org_all.append(city_org_id.City.pk)

                    if int(city_id) in id_from_city_org_all:
                        result.append(item)
            paginator = PageNumberPagination()
            result_page = paginator.paginate_queryset(result, request)
        else:
            paginator = PageNumberPagination()
            result_page = paginator.paginate_queryset(items, request)

        serializer = OrganizationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

