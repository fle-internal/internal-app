from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render

from feedbacks.forms import FeedbackCreationForm
from projects.models import Project

@login_required
def create(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.user not in project.collaborators.all():
        return HttpResponseForbidden(request)

    if request.method == 'POST':
        pass
        # form = FeedbackCreationForm(request.POST)
        # do something with the data
    elif request.method == 'GET':
        form = FeedbackCreationForm()
        form.fields['target'].queryset = project.collaborators
        return render(request, 'feedbacks/create.html', { 'form': form })
