# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from feedbacks import models
from django.views.generic import *
from django.db.models import Avg

class FeedbackList(ListView):
	model = models.Feedback
	context_object_name = 'feedback'
	template_name = 'feedback/view_feedback.html'
