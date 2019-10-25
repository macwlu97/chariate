from django.conf.urls import url
from django.urls import path

from chariate_app import views
from chariate_app.views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView
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

    url(r'^user/(?P<id>[0-9]+)$', views.UserAPIView.as_view()),
    url(r'^user/$', views.UserAPIListView.as_view()),

    url(r'^organization/(?P<id>[0-9]+)$', views.OrganizationAPIView.as_view()),
    url(r'^organization/$', views.OrganizationAPIListView.as_view()),

    url(r'^memberorganization/(?P<id>[0-9]+)$', views.MemberOrganizationAPIView.as_view()),
    url(r'^memberorganization/$', views.MemberOrganizationAPIListView.as_view()),

    url(r'^album/(?P<id>[0-9]+)$', views.AlbumAPIView.as_view()),
    url(r'^album/$', views.AlbumAPIListView.as_view()),

    url(r'^city/(?P<id>[0-9]+)$', views.CityAPIView.as_view()),
    url(r'^city/$', views.CityAPIListView.as_view()),

    url(r'^cityorganization/(?P<id>[0-9]+)$', views.CityOrganizationAPIView.as_view()),
    url(r'^cityorganization/$', views.CityOrganizationAPIListView.as_view()),

    url(r'^dictdecision/(?P<id>[0-9]+)$', views.DictDecisionAPIView.as_view()),
    url(r'^dictdecision/$', views.DictDecisionAPIListView.as_view()),

    url(r'^event/(?P<id>[0-9]+)$', views.EventAPIView.as_view()),
    url(r'^event/$', views.EventAPIListView.as_view()),

    url(r'^information/(?P<id>[0-9]+)$', views.InformationAPIView.as_view()),
    url(r'^information/$', views.InformationAPIListView.as_view()),

    url(r'^like/(?P<id>[0-9]+)$', views.LikeAPIView.as_view()),
    url(r'^like/$', views.LikeAPIListView.as_view()),

    url(r'^observer/(?P<id>[0-9]+)$', views.ObserverAPIView.as_view()),
    url(r'^observer/$', views.ObserverAPIListView.as_view()),

    url(r'^participant/(?P<id>[0-9]+)$', views.ParticipantAPIView.as_view()),
    url(r'^participant/$', views.ParticipantAPIListView.as_view()),

    url(r'^photo/(?P<id>[0-9]+)$', views.PhotoAPIView.as_view()),
    url(r'^photo/$', views.PhotoAPIListView.as_view()),

    url(r'^review/(?P<id>[0-9]+)$', views.ReviewAPIView.as_view()),
    url(r'^review/$', views.ReviewAPIListView.as_view()),
]