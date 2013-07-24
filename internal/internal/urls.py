from django.conf.urls import *
from projects.admin import admin
from projects.models import Project, Collaborator, Leader

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import projects
import profiles


admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile_index/$', profiles.views.profile),
    url(r'^profile/$', profiles.views.profile),
    url(r'^create_project/$', projects.views.create_project),
    url(r'^project_index/$', projects.views.project_index),
    url(r'^project_details/$', projects.views.project_details),
    url(r'^home/', include(admin.site.urls)),
)
