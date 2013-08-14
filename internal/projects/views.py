from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.generic import *
from projects.models import *
from projects.forms import *
from django.contrib.auth.decorators import login_required
from django import forms

#create project page which lets you assign the project name, members, and member positions
@login_required
def create_project(request):
	if request.POST:
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/projects/')
	else:
		form = ProjectForm(initial={ 'widgets': { 'owner': forms.HiddenInput }, 'owner': request.user })


	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('projects/create_project.html', args)

class IndexList(ListView):
	context_object_name = 'index'
	queryset = Project.objects.order_by('-deadline')
	template_name = 'projects/project_index.html'

def details(request, id):
	detail = Project.objects.get(pk=id)
	task = Task.objects.get(pk=id)
	role = Role.objects.get(pk=id)
	return render(request, 'projects/project_detail.html',
			{'detail':detail,
			'task':task,
			'role':role})
