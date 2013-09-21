from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

import feedbacks.urls
import profiles.urls
import projects.urls
import views

admin.autodiscover()

urlpatterns = patterns('',
    url('^$', profiles.urls.profile_index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', views.contact),
    url(r'^dashboard/', views.dashboard),
    url(r'^events/', include('events.urls')),
    url(r'^feedbacks/', include(feedbacks.urls)),
    url(r'^logout/$', 'profiles.views.logout', name='logout'),
    url(r'^profiles/', include(profiles.urls)),
    url(r'^projects/', include(projects.urls)),
    url(r'', include('social_auth.urls')),
)
