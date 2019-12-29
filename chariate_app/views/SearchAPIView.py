from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from chariate_app.models import Organization, CityOrganization, Fundraising, Event
from chariate_app.serializers import OrganizationSerializer
from chariate_app.services import SearchEngine


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
        mode = request.GET.get('sort')
        type = request.GET.get('type')

        result = SearchEngine.execute({
            'search_text': search_text,
            'city_id': city_id,
            'mode': mode,
            'type': type
        })

        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(result, request)

        return paginator.get_paginated_response(result_page)
