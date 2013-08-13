from django.conf.urls import url, patterns
from feedbacks import views

urlpatterns = patterns('',
	url(r'^create/(?P<project_id>\d+)/$', views.create, name='feedback_create'),
	url(r'^(?P<id>\d+)/$', views.FeedbackList.as_view(), name='view_feedback'),
)
