# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from feedbacks.models import *
from django.views.generic import *

class FeedbackList(ListView):
	model = Feedback
	context_object_name = 'feedback'
	template_name = 'feedback/view_feedback.html'

def summary(request):
	avg = Avg.objects.all()
	return render(request, 'profiles/profile.html', {'avg':avg})
