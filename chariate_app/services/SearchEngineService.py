from django.db.models import Q
from service_objects.services import Service
from chariate_app.models import Organization, CityOrganization, Fundraising, Event

class SearchEngine(Service):
    def process(self):
        search_text = self.data['search_text']
        city_id = self.data['city_id']
        type = self.data['type']
        mode = self.data['mode']

        if not type or int(type) in [0, 1]:
            items_organization = Organization.objects.filter(name__contains=search_text)
        if not type or int(type) is 3:
            items_fundraising = Fundraising.objects.filter(title__contains=search_text)

        result = []

        if int(city_id) is not 0:
            if not type or int(type) in [0,1]:
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
                                "add_user": item.add_user_id
                            }

                            if type is '':
                                result.append(new_organization)
                            elif int(new_organization['type']) is int(type):
                                result.append(new_organization)

            if not type or int(type) is 2:
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
                        "title": event.title,
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

            if not type or int(type) in [0, 1]:
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
                        "add_user": item.add_user_id
                    }

                    if type is '':
                        result.append(new_organization)
                    elif int(new_organization['type']) is int(type):
                        result.append(new_organization)

            if not type or int(type) is 2:
                items_event = Event.objects.filter(title__contains=search_text)
                for event in items_event:
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
                        "title": event.title,
                        "start_date": event.start_date,
                        "end_date": event.end_date,
                        "city": city_obj,
                        "organization": org_obj,
                        "add_date": event.add_date,
                        "add_user": event.add_user_id,
                        "type": 2
                    }
                    result.append(new_event)

        if not type or int(type) is 3:
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
                    "name": fundraising.owner_id.first_name + " " + fundraising.owner_id.last_name
                }
                new_fundraising = {
                    "id": fundraising.id,
                    "title": fundraising.title,
                    "start_date": fundraising.start_date,
                    "end_date": fundraising.end_date,
                    "city": city_obj,
                    "add_date": fundraising.add_date,
                    "add_user": fundraising.add_user_id,
                    "organization": org_obj,
                    "owner": owner_obj,
                    "type": 3
                }
                result.append(new_fundraising)

        return result
