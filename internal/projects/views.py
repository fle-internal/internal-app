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
	context_object_name = 'projects'
	queryset = Project.objects.order_by('-deadline')
	template_name = 'projects/project_index.html'

def details(request, id):
	detail = Project.objects.get(pk=id)
	roles= Role.objects.filter(project=detail)
	return render(request, 'projects/project_detail.html',
			{'project':detail,
			'roles':roles})	

@login_required
def join_project(request, id):
    if 'q' in request.GET:
        q = request.GET['q']
	detail = Project.objects.get(pk=id)	
	roles= Role.objects.filter(project=detail)
	#form = Role(request.POST,{'role_name':q,'profile':request.user,'project':detail})
	#form.save()
	#form.save()
	return render_to_response('projects/join_project.html', {'role':q,'collaborator':request.user,'project':detail})
    else:
	    return render_to_response('projects/join_project.html', {'error': True})

def edit_project(request, id):
	detail = Project.objects.get(pk=id)
	roles= Role.objects.filter(project=detail)
	return render_to_response('projects/edit_project.html',)
