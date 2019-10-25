from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

class MemberOrganizationAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = MemberOrganization.objects.get(pk=id)
            serializer = MemberOrganizationSerializer(item)
            return Response(serializer.data)
        except MemberOrganization.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = MemberOrganization.objects.get(pk=id)
        except MemberOrganization.DoesNotExist:
            return Response(status=404)
        serializer = MemberOrganizationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = MemberOrganization.objects.get(pk=id)
        except MemberOrganization.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MemberOrganizationAPIListView(APIView):

    def get(self, request, format=None):
        items = MemberOrganization.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = MemberOrganizationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberOrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)