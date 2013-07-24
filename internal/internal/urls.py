from django.conf.urls import *
from projects import views
from projects.admin import admin
from projects.models import Project, Collaborator, Leader

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

"""create_proj_info = {
	'queryset': Project.objects.all(),
	'template_name': 'create_project.html',
}"""

urlpatterns = patterns('',
	#url(r'^create_project/$', create_proj_info),
	url(r'^create_project/$', views.create_project),
	url(r'^project_index/$', views.project_index),
	url(r'^project_details/$', views.project_details),
	url(r'^home/', include(admin.site.urls)),
)
