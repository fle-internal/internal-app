from django.conf.urls import *
from django.views.generic import *
from projects.models import *
from projects.views import *

urlpatterns = patterns('',

    url(r'^$', IndexList.as_view(), name='project_index'),
    url(r'^(?P<id>\d+)/$', details, name='project_detail'),
    url(r'^create/$', create_project, name='project_create'),
    url(r'^edit(?P<id>\d+)/$', edit_project, name='project_edit'),
 )
	

