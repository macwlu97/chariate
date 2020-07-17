import base64

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Organization, CityOrganization
from chariate_app.serializers import OrganizationSerializer,OrganizationPutSerializer


class OrganizationAPIView(APIView):
    '''
        API for handling organization.
    '''

    def get(self, request, id, format=None):
        '''
            Method returns orgzanization.
        '''
        try:
            item = Organization.objects.get(pk=id)
            serializer = OrganizationSerializer(item)
            return Response(serializer.data)
        except Organization.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        '''
            Method updates organization.
        '''
        try:
            item = Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            return Response(status=404)
        res = request.data
        res['mod_user'] = request.user.id
        serializer = OrganizationPutSerializer(item, data=res)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        '''
            Method deletes organization.
        '''
        try:
            item = Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class OrganizationAPIListView(APIView):
    '''
        API for handling lists of organization methods.
    '''

    def get(self, request, format=None):
        '''
            Method returns list of all organization.
        '''
        items = Organization.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = OrganizationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        '''
            Method creates organization.
        '''
        res = request.data
        res['add_user'] = request.user.id
        res['mod_user'] = request.user.id
        print(res['city_id'])
        serializer = OrganizationSerializer(data=res)

        if serializer.is_valid():
            serializer.save()
            CityOrganization.objects.create(City_id=res['city_id'], Organization_id=serializer.data["id"])

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @api_view(['GET', ])
    def get_my_organization(request, format=None):
        # print(request.user.id)
        user_id = request.user.id
        items = Organization.objects.filter(add_user_id=user_id)
        res = {}
        res["results"]=[]
        for item in items:
            city = CityOrganization.objects.get(Organization=item)
            city_obj = city.City
            city_name = city_obj.name
            type_name = None

            item_type = item.type
            if item_type == 0:
                type_name = "Fundacja"
            elif item_type == 1:
                type_name = "Społeczność"

            # print(city_id)
            # print(city.City)
            obj = {
                "id": item.id,
                "name": item.name,
                "sh_name": item.sh_name,
                "description": item.description,
                "type": item_type,
                "type_name": type_name,
                "city": city_name,
            }
            res["results"].append(obj)

        return Response(res, status=200)

    # '''
    #             Method returns list of all organization.
    #         '''
    # items = Organization.objects.all()
    # paginator = PageNumberPagination()
    # result_page = paginator.paginate_queryset(items, request)
    # serializer = OrganizationSerializer(result_page, many=True)
    # return paginator.get_paginated_response(serializer.data)

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
            item = Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            return Response(status=404)

        request_data = {
            'mod_user': request.user.id,
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
        return Response({"status":"false"}, status=400)

    @api_view(['GET', ])
    def get_cover_image(request, id, format=None):
        try:
            item = Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            return Response(status=404)
        decode = base64.decodebytes(item.logo)
        filetype = item.file_type
        if item.file_type:
            return HttpResponse(decode, content_type=filetype)
        else:
            return Response({"status":"false"}, status=400)
