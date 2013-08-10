# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import ListView

from feedbacks.forms import FeedbackCreationForm
from feedbacks.models import Feedback
from profiles.models import TeamMember
from projects.models import Project

class FeedbackList(ListView):
	model = Feedback
	context_object_name = 'feedback'
	template_name = 'feedback/view_feedback.html'


def summary(request, id):
    person = TeamMember.objects.get(pk=id)
    return render(request, 'profiles/profile.html', {'avg':person.feedback_averages(),
                                                    'overall':overall_feedback_avgs(),
                                                    'person':person}  )


@login_required
def create(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.user not in project.collaborators.all():
        return HttpResponseForbidden(request)

    if request.method == 'POST':
        form = FeedbackCreationForm(request.POST)
        form.fields['target'].queryset = project.collaborators.exclude(pk=request.user.id)
        if form.is_valid():
            data = form.cleaned_data
            f = Feedback()
            f.project = project
            f.target = data['target']
            f.maker = request.user
            f.participation_rating = data['participation_rating']
            f.contribution_rating = data['contribution_rating']
            f.communication_rating = data['communication_rating']
            f.ease_of_working_together_rating = data['ease_of_working_together_rating']
            f.participation_rationale = data['participation_rationale']
            f.contribution_rationale = data['contribution_rationale']
            f.communication_rationale = data['communication_rationale']
            f.ease_of_working_together_rationale = data['ease_of_working_together_rationale']
            f.save()
            # TODO: add message saying feedback creation is successful
            return redirect('project_detail', id=project.id)
        else:
            return render(request, 'feedbacks/create.html', { 'form': form })
    elif request.method == 'GET':
        form = FeedbackCreationForm()
        form.fields['target'].queryset = project.collaborators.exclude(pk=request.user.id)
        return render(request, 'feedbacks/create.html', { 'form': form })
