from django.conf.urls import *
from projects.admin import admin
from projects.models import Project, Collaborator, Leader

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from projects import views as project_views
from profiles import views as profile_views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile_index/$', profile_views.profile_index, name='profile_index'),
    url(r'^profile/$', profile_views.profile),
    url(r'^create_project/$', project_views.create_project),
    url(r'^project_index/$', project_views.project_index),
    url(r'^project_details/$', project_views.project_details),
    url(r'^home/', include(admin.site.urls)),
)
