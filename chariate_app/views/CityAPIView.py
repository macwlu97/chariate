from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

class CityAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = City.objects.get(pk=id)
            serializer = CitySerializer(item)
            return Response(serializer.data)
        except City.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = City.objects.get(pk=id)
        except City.DoesNotExist:
            return Response(status=404)
        serializer = CitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = City.objects.get(pk=id)
        except City.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CityAPIListView(APIView):

    def get(self, request, format=None):
        items = City.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CitySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)