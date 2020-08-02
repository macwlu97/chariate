from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Like, Organization
from chariate_app.serializers import LikeSerializer


class LikeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Like.objects.get(pk=id)
            serializer = LikeSerializer(item)
            return Response(serializer.data)
        except Like.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Like.objects.get(pk=id)
        except Like.DoesNotExist:
            return Response(status=404)
        serializer = LikeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Like.objects.get(pk=id)
        except Like.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LikeAPIListView(APIView):

    def get(self, request, format=None):
        items = Like.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = LikeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @api_view(['GET', ])
    def get_my_like_organization(request, orgId, format=None):
        user_id = request.user.id
        items = Like.objects.filter(organization_id=orgId, add_user_id=user_id)

        print(items)
        count_objects = len(items)
        if count_objects > 0:
            status = {"status":1}
            return Response(status)
        else:
            status = {"status": 0}
            return Response(status)

    @api_view(['GET', ])
    def get_my_like_event(request, eventId, format=None):
        user_id = request.user.id
        items = Like.objects.filter(event_id=eventId, add_user_id=user_id)

        print(items)
        count_objects = len(items)
        if count_objects > 0:
            status = {"status": 1}
            return Response(status)
        else:
            status = {"status": 0}
            return Response(status)

    @api_view(['GET', ])
    def get_my_like_fundraising(request, fundraiserId, format=None):
        user_id = request.user.id
        items = Like.objects.filter(fundraising_id=fundraiserId, add_user_id=user_id)

        print(items)
        count_objects = len(items)
        if count_objects > 0:
            status = {"status": 1}
            return Response(status)
        else:
            status = {"status": 0}
            return Response(status)