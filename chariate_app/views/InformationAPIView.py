from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Information, TypeInformation
from chariate_app.serializers import InformationSerializer


class InformationAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Information.objects.get(pk=id)
            serializer = InformationSerializer(item)
            return Response(serializer.data)
        except Information.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Information.objects.get(pk=id)
        except Information.DoesNotExist:
            return Response(status=404)
        serializer = InformationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Information.objects.get(pk=id)
        except Information.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class InformationAPIListView(APIView):

    def get(self, request, format=None):
        items = Information.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = InformationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @api_view(['GET', ])
    def organization_informations(request, org_id, format=None):
        items = Information.objects.filter(organization_id=org_id)
        # serializer = InformationSerializer(items, many=True)

        res = {}
        res["results"] = []
        for item in items:
            item_type = item.type_info_id
            obj = {
                "id": item.id,
                "name": item_type.text_field,
                "content": item.content,
            }
            res["results"].append(obj)
        return Response(res, status=200)