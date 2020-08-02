from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Like, Organization
from chariate_app.serializers import LikeSerializer
from datetime import timedelta
from django.utils import timezone

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

    #Week
    @api_view(['GET', ])
    def get_popularity_organization(request, format=None):
        user_id = request.user.id
        organizations = Organization.objects.all()

        result = []

        for organization in organizations:
            likesCount = 0
            time_threshold = timezone.now() - timedelta(days=7)
            try:
                likes = Like.objects.all().filter(organization_id=organization.id, add_date__gte=time_threshold)
                likesCount = len(likes)
            except Like.DoesNotExist:
                likesCount = 0

            new_item = {
                "id": organization.id,
                "name": organization.name,
                "likes": likesCount,
                "type": organization.type,
                "description": organization.description
            }
            if likesCount > 0:
                result.append(new_item)

        sorted_result = sorted(result, key=lambda x: x['likes'], reverse=True)
        most_upvoted = sorted_result[:5]

        if most_upvoted:
            return Response(most_upvoted)
        else:
            status = "failed"
            return Response(status)

    #Last day
    @api_view(['GET', ])
    def get_growing_popularity_organization(request, format=None):
        user_id = request.user.id
        organizations = Organization.objects.all()

        result = []

        for organization in organizations:
            likesCount = 0
            time_threshold = timezone.now() - timedelta(days=1)
            try:
                likes = Like.objects.all().filter(organization_id=organization.id, add_date__gte=time_threshold)
                likesCount = len(likes)
            except Like.DoesNotExist:
                likesCount = 0

            new_item = {
                "id": organization.id,
                "name": organization.name,
                "likes": likesCount,
                "type": organization.type,
                "description": organization.description
            }
            if likesCount > 0:
                result.append(new_item)

        sorted_result = sorted(result, key=lambda x: x['likes'], reverse=True)
        most_upvoted = sorted_result[:5]

        if most_upvoted:
            return Response(most_upvoted)
        else:
            status = "failed"
            return Response(status)

    # Week
    @api_view(['GET', ])
    def get_last_added_organization(request, format=None):
        user_id = request.user.id
        time_threshold = timezone.now() - timedelta(days=7)
        organizations = Organization.objects.all().filter(add_date__gte=time_threshold)

        result = []

        for organization in organizations:
            likesCount = 0

            try:
                likes = Like.objects.all().filter(organization_id=organization.id)
                likesCount = len(likes)
            except Like.DoesNotExist:
                likesCount = 0

            new_item = {
                "id": organization.id,
                "name": organization.name,
                "likes": likesCount,
                "add_date": organization.add_date,
                "type": organization.type,
                "description": organization.description
            }
            # if likesCount > 0:
            result.append(new_item)

        sorted_result = sorted(result, key=lambda x: x['add_date'], reverse=True)
        # most_upvoted = sorted_result[:5]
        print(sorted_result)
        if sorted_result:
            return Response(sorted_result)
        else:
            status = "failed"
            return Response(status)

    # Week
    @api_view(['GET', ])
    def get_new_organization(request, format=None):
        user_id = request.user.id
        time_threshold = timezone.now() - timedelta(days=1)
        organizations = Organization.objects.all().filter(add_date__gte=time_threshold)

        result = []

        for organization in organizations:
            likesCount = 0

            try:
                likes = Like.objects.all().filter(organization_id=organization.id)
                likesCount = len(likes)
            except Like.DoesNotExist:
                likesCount = 0

            new_item = {
                "id": organization.id,
                "name": organization.name,
                "likes": likesCount,
                "add_date": organization.add_date,
                "type": organization.type,
                "description": organization.description
            }
            # if likesCount > 0:
            result.append(new_item)

        sorted_result = sorted(result, key=lambda x: x['add_date'], reverse=True)
        # most_upvoted = sorted_result[:5]

        if sorted_result:
            return Response(sorted_result)
        else:
            status = "failed"
            return Response(status)

    @api_view(['GET', ])
    def get_my_favorites_organization(request, format=None):
        user_id = request.user.id
        organizations = Organization.objects.all()

        result = []

        for organization in organizations:
            likesCount = 0

            try:
                likes = Like.objects.all().filter(organization_id=organization.id, add_user_id=user_id)
                likesCount = len(likes)
            except Like.DoesNotExist:
                likesCount = 0

            new_item = {
                "id": organization.id,
                "name": organization.name,
                "likes": likesCount,
                "type": organization.type,
                "description": organization.description
            }
            if likesCount > 0:
                result.append(new_item)

        sorted_result = sorted(result, key=lambda x: x['likes'], reverse=True)
        # most_upvoted = sorted_result[:5]

        if sorted_result:
            return Response(sorted_result)
        else:
            status = "failed"
            return Response(status)