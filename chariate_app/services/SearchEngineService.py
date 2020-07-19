import base64

from django.db.models import Q
from service_objects.services import Service
from chariate_app.models import Organization, CityOrganization, Fundraising, Event

class SearchEngine(Service):
    def process(self):
        search_text = self.data['search_text']
        city_id = self.data['city_id']
        type = self.data['type']
        mode = self.data['mode']

        if not type or int(type) in [0, 1, 5]:
            items_organization = Organization.objects.filter(name__contains=search_text)
        if not type or int(type) in [3,5]:
            items_fundraising = Fundraising.objects.filter(title__contains=search_text)

        result = []

        if int(city_id) is not 0:
            if not type or int(type) in [0,1, 5]:
                for item in items_organization:
                    try:
                        city_org_all = CityOrganization.objects.all().filter(Organization_id=item.id)
                    except CityOrganization.DoesNotExist:
                        city_org_id = 0

                    id_from_city_org_all = []
                    if city_org_all:
                        for city_org_id in city_org_all:
                            id_from_city_org_all.append(city_org_id.City.pk)

                        if int(city_id) in id_from_city_org_all:

                            if city_org_all:
                                final_list = []
                                for city_org in city_org_all:
                                    dict = {
                                        "id": city_org.City.pk,
                                        "name": city_org.City.name
                                    }
                                    final_list.append(dict)

                            new_organization = {
                                "id": item.id,
                                "name": item.name,
                                "sh_name": item.sh_name,
                                "description": item.description,
                                "city": final_list,
                                "type": item.type,
                                "add_date": item.add_date,
                                "add_user": item.add_user_id,
                            }

                            if type is '' or type is None or int(type) is 5:
                                result.append(new_organization)
                            elif int(new_organization['type']) is int(type):
                                result.append(new_organization)

            if not type or int(type) in [2,5]:
                items_event = Event.objects.filter(Q(title__contains=search_text) & Q(city_id=city_id))
                for event in items_event:
                    city_obj = {
                        "id": event.city_id_id,
                        "name": event.city_id.name
                    }
                    org_obj = {
                        "id": event.organization_id_id,
                        "name": event.organization_id.name,
                        "description": event.organization_id.description
                    }
                    new_event = {
                        "id": event.id,
                        "name": event.title,
                        "start_date": event.start_date,
                        "end_date": event.end_date,
                        "city": city_obj,
                        "organization": org_obj,
                        "add_date": event.add_date,
                        "add_user": event.add_user_id,
                        "type": 2
                    }
                    result.append(new_event)
        else:

            if not type or int(type) in [0, 1, 5]:
                for item in items_organization:
                    city_list = []
                    try:
                        city_org_all = CityOrganization.objects.all().filter(Organization_id=item.id)
                        id_from_city_org_all = []
                        if city_org_all:
                            for city_org_id in city_org_all:
                                id_from_city_org_all.append(city_org_id.City.pk)

                            if id_from_city_org_all:

                                if city_org_all:
                                    final_list = []
                                    for city_org in city_org_all:
                                        dict = {
                                            "id": city_org.City.pk,
                                            "name": city_org.City.name
                                        }
                                        city_list.append(dict)
                    except CityOrganization.DoesNotExist:
                        print("CityOrganization.DoesNotExist")

                    if not city_list:
                        city_obj = {
                                "id": 0,
                                "name": "Polska"
                            }
                        city_list.append(city_obj)

                    new_organization = {
                        "id": item.id,
                        "name": item.name,
                        "sh_name": item.sh_name,
                        "description": item.description,
                        "city": city_list,
                        "type": item.type,
                        "add_date": item.add_date,
                        "add_user": item.add_user_id,
                    }

                    if type is '' or type is None or int(type) is 5:
                        result.append(new_organization)
                    elif int(new_organization['type']) is int(type):
                        result.append(new_organization)

            if not type or int(type) in [2,5]:
                items_event = Event.objects.filter(title__contains=search_text)
                for event in items_event:
                    date_event = str(event.start_date).split(" ")[0]
                    time_event = str(event.start_date.hour) + ":" + str(event.start_date.minute)
                    add_date_event = str(event.add_date).split(" ")[0]

                    if event.city_id:
                        city_obj = {
                            "id": event.city_id_id,
                            "name": event.city_id.name
                        }
                    else:
                        city_obj = {
                            "id": 0,
                            "name": "Polska"
                        }
                    org_obj = {
                        "id": event.organization_id_id,
                        "name": event.organization_id.name,
                        "description": event.organization_id.description
                    }
                    new_event = {
                        "id": event.id,
                        "name": event.title,
                        "start_date": date_event,
                        "start_time": time_event,
                        "end_date": event.end_date,
                        "city": city_obj,
                        "organization": org_obj,
                        "add_date": add_date_event,
                        "add_user": event.add_user_id,
                        "type": 2
                    }
                    result.append(new_event)

        if not type or int(type) in [3,5]:
            for fundraising in items_fundraising:
                city_obj = [{
                    "id": 0,
                    "name": "Polska"
                }]
                org_obj = {
                    "id": fundraising.organization_id_id,
                    "name": fundraising.organization_id.name,
                    "description": fundraising.organization_id.description
                }
                owner_obj = {
                    "id": fundraising.owner_id_id,
                    # "name": fundraising.owner_id.first_name + " " + fundraising.owner_id.last_name
                }

                date_fundraising = str(fundraising.end_date).split(" ")[0]
                time_fudraising = str(fundraising.end_date.hour) + ":" + str(fundraising.end_date.minute)
                add_date_fundraising = str(fundraising.add_date).split(" ")[0]

                new_fundraising = {
                    "id": fundraising.id,
                    "name": fundraising.title,
                    "description": fundraising.description,
                    "start_date": fundraising.start_date,
                    "end_date": date_fundraising,
                    "end_time": time_fudraising,
                    "city": city_obj,
                    "add_date": add_date_fundraising,
                    "add_user": fundraising.add_user_id,
                    "organization": org_obj,
                    "owner": owner_obj,
                    "type": 3
                }
                result.append(new_fundraising)

        if mode and str(mode) == 'name':
            sorted_result = sorted(result, key=lambda x: x['name'])
            return sorted_result
        elif mode and str(mode) == 'popularity':
            return result
        elif mode and str(mode) == "date":
            sorted_result = sorted(result, key=lambda x: x['add_date'])
            return sorted_result
        elif not mode or str(mode) == "none":
            return result
