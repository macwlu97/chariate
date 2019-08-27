from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Organization
from chariate_app.serializers import OrganizationSerializer


class DictActorAPIView(APIView):
    '''
        API for handling organization.
    '''

    def get(self, request, id, format=None):
        '''
            Method returns orgzanization.
        '''
        try:
            item = Organization.objects.get(pk=id)
            serializer = OrganizationSerializer(item)
            return Response(serializer.data)
        except Organization.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        '''
            Method updates organization.
        '''
        try:
            item = Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            return Response(status=404)
        res = request.data
        res['mod_user'] = request.user.id
        serializer = OrganizationSerializer(item, data=res)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        '''
            Method deletes organization.
        '''
        try:
            item = Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DictActorAPIListView(APIView):
    '''
        API for handling lists of organization methods.
    '''

    def get(self, request, format=None):
        '''
            Method returns list of all organization.
        '''
        items = Organization.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = OrganizationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        '''
            Method creates organization.
        '''
        res = request.data
        res['add_user'] = request.user.id
        res['mod_user'] = request.user.id
        serializer = OrganizationSerializer(data=res)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
