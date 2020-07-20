import base64

from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import City, Organization, CityOrganization
from chariate_app.serializers import CitySerializer
from rest_framework.decorators import api_view

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

    @api_view(['GET', ])
    def num_organization(request, format=None):
        items = City.objects.all()
        res = {}
        res["results"]=[]
        for item in items:
            org_in_city = CityOrganization.objects.filter(City=item)
            obj = {
                "id": item.id,
                "name": item.name,
                "sum_organization": len(org_in_city),
            }
            res["results"].append(obj)
        return Response(res, status=200)

    @api_view(['PUT', ])
    def upload_cover_image(request, id, format=None):
        uploaded_file = request.FILES['file']
        bytes = base64.encodebytes(uploaded_file.read())
        filename = str(uploaded_file)
        print(bytes)
        '''
            Method updates organization cover image.
        '''

        try:
            item = City.objects.get(pk=id)
        except City.DoesNotExist:
            return Response(status=404)

        request_data = {
            # 'mod_user': request.user.id,
            'logo': bytes
        }

        fileType = None
        if filename.endswith('.png'):
            fileType = "image/png"
        elif filename.endswith('.jpeg'):
            fileType = "image/jpeg"
        elif filename.endswith('.jpg'):
            fileType = "image/jpeg"
        else:
            fileType = None

        if bytes:
            item.logo = bytes
            item.file_type = fileType
            item.save()
            return Response({"status": "saved"}, status=200)
        return Response({"status": "false"}, status=400)

    @api_view(['GET', ])
    def get_cover_image(request, id, format=None):
        try:
            item = City.objects.get(pk=id)
        except City.DoesNotExist:
            return Response(status=404)
        decode = base64.decodebytes(item.logo)
        filetype = item.file_type
        if item.file_type:
            return HttpResponse(decode, content_type=filetype)
        else:
            return Response({"status":"false"}, status=400)