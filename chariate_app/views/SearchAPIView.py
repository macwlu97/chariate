from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Organization
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
            Method returns search results. city_id, search_text,
        '''
        search_text = request.GET.get('q')
        search_query = Q(add_user=2) & Q(name__contains=search_text)
        items = Organization.objects.filter(search_query)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = OrganizationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

