from django.conf.urls import url, patterns

urlpatterns = patterns("",
    url(r'^create/(?P<project_id>\d+)/$', 'feedbacks.views.create', name='feedback_create')
)
