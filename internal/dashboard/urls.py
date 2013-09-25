from django.conf.urls import *

urlpatterns = patterns('',
    url('^$', 'dashboard.views.dashboard'),
)
