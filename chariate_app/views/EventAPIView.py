from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from chariate_app.models import Event, City
from chariate_app.serializers import EventSerializer
import datetime

class EventAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Event.objects.get(pk=id)
            date_event = str(item.start_date).split(" ")[0]
            time_event = str(item.start_date.hour) + ":" + str(item.start_date.minute)

            weekDays = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")

            format_str = '%Y-%m-%d'  # The format date
            format_time_str = '%H:%M'  # The format time
            datetime_obj = datetime.datetime.strptime(date_event, format_str)
            time_obj = datetime.datetime.strptime(time_event, format_time_str)
            date_event = datetime_obj.strftime("%m/%d/%Y")
            time_event = time_obj.strftime("%H:%M")
            weekday = datetime_obj.weekday()
            weekday_as_string = weekDays[weekday]

            item.start_date = '{weekday}, {date_event}, o {time_event}'.format(weekday=weekday_as_string, date_event=date_event, time_event=time_event)

            serializer = EventSerializer(item)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Event.objects.get(pk=id)
        except Event.DoesNotExist:
            return Response(status=404)
        serializer = EventSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Event.objects.get(pk=id)
        except Event.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EventAPIListView(APIView):

    def get(self, request, format=None):
        items = Event.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EventSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @api_view(['GET', ])
    def get_events_organization(request, org_id,format=None):
        items = Event.objects.filter(organization_id=org_id)
        res = {}
        res["results"] = []
        for item in items:
            date_event = str(item.start_date).split(" ")[0]
            time_event = str(item.start_date.hour) + ":" + str(item.start_date.minute)
            add_date_event = str(item.add_date).split(" ")[0]
            obj = {
                "id": item.id,
                "name": item.title,
                "organization_id": item.organization_id_id,
                "organization_name": item.organization_id.name,
                "start_date": date_event,
                "time_event": time_event,
            }
            res["results"].append(obj)

        return Response(res, status=200)