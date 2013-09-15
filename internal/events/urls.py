from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^github/$',  'events.views.github', name='github_event'),
)
