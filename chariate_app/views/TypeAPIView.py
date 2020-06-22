from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import TypeInformation
from chariate_app.serializers import TypeInformationSerializer
from rest_framework.decorators import api_view

class TypeInformationAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = TypeInformation.objects.get(pk=id)
            serializer = TypeInformationSerializer(item)
            return Response(serializer.data)
        except TypeInformation.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TypeInformation.objects.get(pk=id)
        except TypeInformation.DoesNotExist:
            return Response(status=404)
        serializer = TypeInformationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TypeInformation.objects.get(pk=id)
        except TypeInformation.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TypeInformationAPIListView(APIView):

    def get(self, request, format=None):
        items = TypeInformation.objects.all()
        # paginator = PageNumberPagination()
        # result_page = paginator.paginate_queryset(items, request)
        serializer = TypeInformationSerializer(items, many=True)
        response = {"results": serializer.data}
        return Response(response)

    def post(self, request, format=None):
        serializer = TypeInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)