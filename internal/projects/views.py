from django import forms
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic import *

from projects.forms import RoleForm, ProjectForm
from projects.models import *

@login_required
def create_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save()
            return HttpResponseRedirect(reverse('project_detail', args=[project.id]))
        else:
            return render(request, 'projects/create_project.html',
                          {'project_form': project_form})
    else:
        project_form = ProjectForm(initial={'widgets': {'owner': forms.HiddenInput},
                                            'owner': request.user})

    return render(request, 'projects/create_project.html',
                  {'project_form': project_form})

@login_required
def join_project(request, id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project_detail', args=[id]))
        else:
            return render(request, 'projects/join_project.html', {'form': form})
    else:
        form = RoleForm(initial={'profile': request.user, 'project': project})
        return render(request, 'projects/join_project.html', {'form': form})


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
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project_index'))
        else:
            return render(request, 'projects/edit_project.html', {'form': form})
    else:
        form = ProjectForm(instance=project)
        return render(request, 'projects/edit_project.html', {'form': form})
