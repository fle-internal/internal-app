from django.shortcuts import render
from django.http import HttpResponse
from projects.models import *
from django.views.generic import *

#create project page which lets you assign the project name, members, and member positions
def create_project(request):
	return render(request, 'projects/create_project.html', {})

class IndexList(ListView):
	pass

def project_index(request):
	return render(request, 'projects/project_index.html', {})

"""class DetailsList(ListView):
	model = Project
	template_name = 'projects/project_detail.html'
	context_object_name = 'details'"""

def details(request, id):
	detail = Project.objects.all()
	task = Task.objects.all()
	role = Role.objects.all()
	return render(request, 'projects/project_detail.html',
			{'detail':detail,
			'task':task,
			'role':role})
