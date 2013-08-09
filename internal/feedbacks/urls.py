from django.conf.urls import *
from django.views.generic import *
from feedbacks.models import *
from feedbacks.views import *

urlpatterns = patterns('',

    url(r'^(?P<id>\d+)/$', FeedbackList.as_view(), name='view_feedback'),

)
