from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from profiles.models import TeamMember


@login_required
def profile(request, id):
    person = TeamMember.objects.get(pk=id)
    return render(request, 'profiles/profile.html', {'person': person})


def profile_index(request):
    persons = TeamMember.objects.all()
    return render(request, 'profiles/profile_index.html', {'persons': persons})


def profile_new(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'profiles/signup.html', {'form': UserCreationForm()})
    else:
        username = request.POST['username']
        if request.POST['password1'] == request.POST['password2']:
            password = request.POST['password1']
        else:
            pass  # How to generate those alerts?
        newuser = TeamMember.objects.create_user(username, password)
        # Should I now check if user has been created?
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'profiles/profile.html', {'person': user})
        else:
            pass  # Return an 'invalid login' error message.

def logout(request):
    return logout_then_login(request)
