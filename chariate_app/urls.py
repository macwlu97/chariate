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
]