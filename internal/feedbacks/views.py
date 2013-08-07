# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from feedbacks import models
from django.views.generic import *

class FeedbackList(ListView):
	model = models.Feedback
	context_object_name = 'feedback'
	template_name = 'feedback/view_feedback.html'

def summary(request, id):
	person = TeamMember.objects.get(pk=id)
	avg = models.Feedback.objects.all()
	return render(request, 'profiles/profile.html', {'avg':avg, 'person':person})
