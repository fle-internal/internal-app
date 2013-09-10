from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.generic import *
from projects.models import *
from projects.forms import *
from django.contrib.auth.decorators import login_required
from django import forms

from projects.forms import RoleForm

@login_required
def create_project(request):
        if request.POST:
                form = ProjectForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/projects/')
        else:
                form = ProjectForm(initial={'widgets': {'owner': forms.HiddenInput}, 'owner': request.user})

        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('projects/create_project.html', args)


class IndexList(ListView):
        context_object_name = 'projects'
        queryset = Project.objects.order_by('-deadline')
        template_name = 'projects/project_index.html'


@login_required
def details(request, id):
        detail = Project.objects.get(pk=id)
        roles= Role.objects.filter(project=detail)
        if request.method == 'GET':
            form = RoleForm(initial={ 'profile': request.user, 'project': detail})
            return render(request, 'projects/project_detail.html',
                            {'project':detail,
                             'form': form,
                            'roles':roles})
        elif request.method == 'POST':
            form = RoleForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'projects/project_detail.html',
                                {'project':detail,
                                 'form': form,
                                'roles':roles})
            else:
                return render(request, 'projects/project_detail.html',
                                {'project':detail,
                                 'form': form,
                                'roles':roles})

@login_required
def edit_project(request, id):
        detail = Project.objects.get(pk=id)
        roles= Role.objects.filter(project=detail)
        return render_to_response('projects/edit_project.html',)
