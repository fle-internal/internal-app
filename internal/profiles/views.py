from django.contrib.auth import get_user_model
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render

from profiles.models import TeamMember
from feedbacks.models import Feedback

def feedback_averages(self):
	if Feedback.objects.filter(target_id=self.id).count() > 0:
		return Feedback.objects.filter(target_id=self.id).aggregate(Avg('participation_rating'),
                                                                    Avg('contribution_rating'),
                                                                    Avg('communication_rating'),
                                                                    Avg('ease_of_working_together_rating'))
	else:
		return 0

def overall_feedback_avgs(self):
	if Feedback.objects.filter(target_id=self.id).count() > 0:
		avgs = self.feedback_averages()
		return (avgs['participation_rating__avg']
            + avgs['contribution_rating__avg'] 
            + avgs['communication_rating__avg'] 
            + avgs['ease_of_working_together_rating__avg'])/4
	else:
		return 0

def profile(request, id):
    	person = TeamMember.objects.get(pk=id)
	return render(request,'profiles/profile.html', {'person': person,
													'avg':person.feedback_averages(),
                                                    'overall':person.overall_feedback_avgs()})

def profile_index(request):
        persons = TeamMember.objects.all()
        return render(request, 'profiles/profile_index.html', { 'persons': persons})

def logout(request):
        return logout_then_login(request)