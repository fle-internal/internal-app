from django.conf.urls import *

from projects import views

urlpatterns = patterns('',
    url(r'', views.project_index, name='project_index'),
    url(r'(?P<id>\d+)$', views.project_details, name='project_detail'),
    url(r'create$', views.create_project, name='project_create'),
)
