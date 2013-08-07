from django.conf.urls import *
from django.views.generic import *
from feedbacks import models
from feedbacks import views

urlpatterns = patterns('',

    url(r'^$', views.FeedbackList.as_view()),

)
