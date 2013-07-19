from django.conf.urls import *
from projects.views import *
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
	url(r'^create_project/$', create_project),
	url(r'^project_index/$', project_index),
	url(r'^project_details/$', project_details),
    # Examples:
    # url(r'^$', 'kalite_internal.views.home', name='home'),
    # url(r'^kalite_internal/', include('kalite_internal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^home/', include(admin.site.urls)),
)
