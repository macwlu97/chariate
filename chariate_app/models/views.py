from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from chariate_app.serializers import UserSerializer, OrganizationSerializer, MemberOrganizationSerializer, AlbumSerializer, CitySerializer, CityOrganizationSerializer, DictDecisionSerializer, EventSerializer, InformationSerializer, LikeSerializer, ObserverSerializer, ParticipantSerializer, PhotoSerializer, ReviewSerializer
from chariate_app.models import User, Organization, MemberOrganization, Album, City, CityOrganization, DictDecision, Event, Information, Like, Observer, Participant, Photo, Review


# class UserAPIView(APIView):
#
#     def get(self, request, id, format=None):
#         try:
#             item = User.objects.get(pk=id)
#             serializer = UserSerializer(item)
#             return Response(serializer.data)
#         except User.DoesNotExist:
#             return Response(status=404)
#
#     def put(self, request, id, format=None):
#         try:
#             item = User.objects.get(pk=id)
#         except User.DoesNotExist:
#             return Response(status=404)
#         serializer = UserSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, id, format=None):
#         try:
#             item = User.objects.get(pk=id)
#         except User.DoesNotExist:
#             return Response(status=404)
#         item.delete()
#         return Response(status=204)
#
#
# class UserAPIListView(APIView):
#
#     def get(self, request, format=None):
#         items = User.objects.all()
#         paginator = PageNumberPagination()
#         result_page = paginator.paginate_queryset(items, request)
#         serializer = UserSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# class OrganizationAPIView(APIView):
#
#     def get(self, request, id, format=None):
#         try:
#             item = Organization.objects.get(pk=id)
#             serializer = OrganizationSerializer(item)
#             return Response(serializer.data)
#         except Organization.DoesNotExist:
#             return Response(status=404)
#
#     def put(self, request, id, format=None):
#         try:
#             item = Organization.objects.get(pk=id)
#         except Organization.DoesNotExist:
#             return Response(status=404)
#         serializer = OrganizationSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, id, format=None):
#         try:
#             item = Organization.objects.get(pk=id)
#         except Organization.DoesNotExist:
#             return Response(status=404)
#         item.delete()
#         return Response(status=204)
#
#
# class OrganizationAPIListView(APIView):
#
#     def get(self, request, format=None):
#         items = Organization.objects.all()
#         paginator = PageNumberPagination()
#         result_page = paginator.paginate_queryset(items, request)
#         serializer = OrganizationSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = OrganizationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)




























