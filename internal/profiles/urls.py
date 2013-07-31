from django.conf.urls import *

from profiles import views

urlpatterns = patterns('',
    url(r'^$', views.profile_index, name='profile_index'),
    url(r'(?P<id>\d+)/$', views.profile, name='profile_detail'),
)
