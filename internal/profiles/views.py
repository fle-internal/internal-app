from django.contrib.auth import get_user_model
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render

User = get_user_model()

def profile(request):
	return render(request,'profiles/profile.html') #edit

def profile_index(request):
        persons = ['jamie', 'ben', 'richard', 'dylan', 'rui']
        imgs = ['profiles/img/{}.jpg'.format(person) for person in persons]
        return render(request,'profiles/profile_index.html', {'imgs': imgs} ) #edit if we decide to populate data.

def logout(request):
        return logout_then_login(request)
