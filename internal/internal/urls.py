from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import profiles.urls
import projects.urls


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'internal/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name' : 'internal/logout.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/', include(profiles.urls)),
    url(r'^projects/', include(projects.urls)),
)
