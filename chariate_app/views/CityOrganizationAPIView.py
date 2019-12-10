from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import CityOrganization
from chariate_app.serializers import CityOrganizationSerializer


class CityOrganizationAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = CityOrganization.objects.get(pk=id)
            serializer = CityOrganizationSerializer(item)
            return Response(serializer.data)
        except CityOrganization.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = CityOrganization.objects.get(pk=id)
        except CityOrganization.DoesNotExist:
            return Response(status=404)
        serializer = CityOrganizationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = CityOrganization.objects.get(pk=id)
        except CityOrganization.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CityOrganizationAPIListView(APIView):

    def get(self, request, format=None):
        items = CityOrganization.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CityOrganizationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CityOrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
