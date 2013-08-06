from django.contrib.auth import get_user_model
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render

from profiles.models import TeamMember

def profile(request, id):
        person = TeamMember.objects.get(pk=id)
	return render(request,'profiles/profile.html', {'person': person})

def profile_index(request):
        persons = TeamMember.objects.all()
        return render(request, 'profiles/profile_index.html', { 'persons': persons})

def logout(request):
        return logout_then_login(request)
        
