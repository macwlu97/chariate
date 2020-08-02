from django.conf.urls import url
from django.urls import path

from chariate_app import views
from chariate_app.views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView
from rest_framework_jwt.views import refresh_jwt_token

from . import views

try:
    from django.conf.urls import patterns
except ImportError:
    pass

app_name = 'chariate_app'

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'create/$', CreateUserAPIView.as_view()),
    url(r'update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'obtain_token/$', authenticate_user, name='authenticate_user'),
    url(r'api-token-refresh/$', refresh_jwt_token, name='refresh_jwt_token'),

    url(r'^user/(?P<id>[0-9]+)$', views.UserAPIView.as_view()),
    url(r'^user/$', views.UserAPIListView.as_view()),

    url(r'^organization/(?P<id>[0-9]+)$', views.OrganizationAPIView.as_view()),
    url(r'^organization/$', views.OrganizationAPIListView.as_view()),
    url(r'^organization/me/$', views.OrganizationAPIListView.get_my_organization, name='get_my_organization'),
    url(r'^organization/upload_cover_image/(?P<id>[0-9]+)$', views.OrganizationAPIListView.upload_cover_image, name='upload_cover_image'),
    url(r'^organization/get_cover_image/(?P<id>[0-9]+)$', views.OrganizationAPIListView.get_cover_image, name='get_cover_image'),

    url(r'^memberorganization/(?P<id>[0-9]+)$', views.MemberOrganizationAPIView.as_view()),
    url(r'^memberorganization/$', views.MemberOrganizationAPIListView.as_view()),

    url(r'^album/(?P<id>[0-9]+)$', views.AlbumAPIView.as_view()),
    url(r'^album/$', views.AlbumAPIListView.as_view()),

    url(r'^city/(?P<id>[0-9]+)$', views.CityAPIView.as_view()),
    url(r'^city/$', views.CityAPIListView.as_view()),
    url(r'^city/num_organization/$',
        views.CityAPIListView.num_organization, name='num_organization'),
    url(r'^city/upload_cover_image/(?P<id>[0-9]+)$', views.CityAPIListView.upload_cover_image, name='upload_cover_image'),
    url(r'^city/get_cover_image/(?P<id>[0-9]+)$', views.CityAPIListView.get_cover_image, name='get_cover_image'),

    url(r'^cityorganization/(?P<id>[0-9]+)$', views.CityOrganizationAPIView.as_view()),
    url(r'^cityorganization/$', views.CityOrganizationAPIListView.as_view()),

    url(r'^dictdecision/(?P<id>[0-9]+)$', views.DictDecisionAPIView.as_view()),
    url(r'^dictdecision/$', views.DictDecisionAPIListView.as_view()),

    url(r'^event/(?P<id>[0-9]+)$', views.EventAPIView.as_view()),
    url(r'^event/$', views.EventAPIListView.as_view()),
    url(r'^event/organization/(?P<org_id>[0-9]+)$', views.EventAPIListView.get_events_organization, name='get_events_organization'),

    url(r'^information/(?P<id>[0-9]+)$', views.InformationAPIView.as_view()),
    url(r'^information/$', views.InformationAPIListView.as_view()),
    url(r'^information/organization/(?P<org_id>[0-9]+)$', views.InformationAPIListView.organization_informations, name='organization_informations'),
    url(r'^information/event/(?P<event_id>[0-9]+)$', views.InformationAPIListView.event_informations, name='event_informations'),
    url(r'^information/fundraising/(?P<fundraising_id>[0-9]+)$', views.InformationAPIListView.fundraising_informations, name='fundraising_informations'),

    url(r'^like/(?P<id>[0-9]+)$', views.LikeAPIView.as_view()),
    url(r'^like/$', views.LikeAPIListView.as_view()),
    url(r'^like/organization/(?P<orgId>[0-9]+)$', views.LikeAPIListView.get_my_like_organization, name='get_my_like_organization'),
    url(r'^like/event/(?P<eventId>[0-9]+)$', views.LikeAPIListView.get_my_like_event, name='get_my_like_event'),
    url(r'^like/fundraising/(?P<fundraiserId>[0-9]+)$', views.LikeAPIListView.get_my_like_fundraising, name='get_my_like_fundraising'),
    url(r'^like/popularity-organizations/$', views.LikeAPIListView.get_popularity_organization, name='get_popularity_organization'),
    url(r'^like/favorites-organizations/$', views.LikeAPIListView.get_my_favorites_organization, name='get_my_favorites_organization'),
    url(r'^like/growing-popularity-organizations/$', views.LikeAPIListView.get_growing_popularity_organization, name='get_growing_popularity_organization'),
    url(r'^like/last-added-organizations/$', views.LikeAPIListView.get_last_added_organization, name='get_last_added_organization'),
    url(r'^like/new-organizations/$', views.LikeAPIListView.get_new_organization, name='get_new_organization'),

    url(r'^observer/(?P<id>[0-9]+)$', views.ObserverAPIView.as_view()),
    url(r'^observer/$', views.ObserverAPIListView.as_view()),

    url(r'^participant/(?P<id>[0-9]+)$', views.ParticipantAPIView.as_view()),
    url(r'^participant/$', views.ParticipantAPIListView.as_view()),

    url(r'^photo/(?P<id>[0-9]+)$', views.PhotoAPIView.as_view()),
    url(r'^photo/$', views.PhotoAPIListView.as_view()),

    url(r'^review/(?P<id>[0-9]+)$', views.ReviewAPIView.as_view()),
    url(r'^review/$', views.ReviewAPIListView.as_view()),

    url(r'^fundraising/(?P<id>[0-9]+)$', views.FundraisingAPIView.as_view()),
    url(r'^fundraising/$', views.FundraisingAPIListView.as_view()),
    url(r'^fundraising/organization/(?P<org_id>[0-9]+)$', views.FundraisingAPIListView.get_fundraising_organization, name='get_fundraising_organization'),

    url(r'^search/(?P<city_id>[0-9]+)$', views.SearchAPIListView.as_view()), #(?P<search_text>[\w\-]+)

    url(r'^typeinformation/(?P<id>[0-9]+)$', views.TypeInformationAPIView.as_view()),
    url(r'^typeinformation/$', views.TypeInformationAPIListView.as_view()),
]