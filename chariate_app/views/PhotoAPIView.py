from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Photo
from chariate_app.serializers import PhotoSerializer


class PhotoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Photo.objects.get(pk=id)
            serializer = PhotoSerializer(item)
            return Response(serializer.data)
        except Photo.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Photo.objects.get(pk=id)
        except Photo.DoesNotExist:
            return Response(status=404)
        serializer = PhotoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Photo.objects.get(pk=id)
        except Photo.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PhotoAPIListView(APIView):

    def get(self, request, format=None):
        items = Photo.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PhotoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
