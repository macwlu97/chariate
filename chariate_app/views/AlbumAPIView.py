from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Album
from chariate_app.serializers import AlbumSerializer


class AlbumAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Album.objects.get(pk=id)
            serializer = AlbumSerializer(item)
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Album.objects.get(pk=id)
        except Album.DoesNotExist:
            return Response(status=404)
        serializer = AlbumSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Album.objects.get(pk=id)
        except Album.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AlbumAPIListView(APIView):

    def get(self, request, format=None):
        items = Album.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AlbumSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
