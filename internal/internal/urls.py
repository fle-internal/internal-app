from django.conf.urls import *
from projects import views
from projects.admin import admin
from projects.models import Project, Collaborator, Leader

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from profiles import views


admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile_index/$', views.profile),
    url(r'^profile/$', views.profile),
    url(r'^create_project/$', views.create_project),
    url(r'^project_index/$', views.project_index),
    url(r'^project_details/$', views.project_details),
    url(r'^home/', include(admin.site.urls)),
)
