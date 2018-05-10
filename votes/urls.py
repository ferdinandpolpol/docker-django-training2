from django.conf.urls import url

from . import views

app_name = 'votes'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<position_id>[0-9]+)/vote/$', views.vote, name='vote'),
]