from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Fundraising
from chariate_app.serializers import FundraisingSerializer


class FundraisingAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Fundraising.objects.get(pk=id)
            serializer = Fundraising(item)
            return Response(serializer.data)
        except Fundraising.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Fundraising.objects.get(pk=id)
        except Fundraising.DoesNotExist:
            return Response(status=404)
        serializer = FundraisingSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Fundraising.objects.get(pk=id)
        except Fundraising.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class FundraisingAPIListView(APIView):

    def get(self, request, format=None):
        items = Fundraising.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = FundraisingSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = FundraisingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @api_view(['GET', ])
    def get_fundraising_organization(request, org_id, format=None):
        items = Fundraising.objects.filter(organization_id=org_id)
        res = {}
        res["results"] = []
        for item in items:
            date_fundraising = str(item.end_date).split(" ")[0]
            time_fudraising = str(item.end_date.hour) + ":" + str(item.end_date.minute)
            add_date_fundraising = str(item.add_date).split(" ")[0]
            obj = {
                "id": item.id,
                "name": item.title,
                "organization_id": item.organization_id_id,
                "organization_name": item.organization_id.name,
                "start_date": date_fundraising,
                "time_fundraising": time_fudraising,
            }
            res["results"].append(obj)

        return Response(res, status=200)