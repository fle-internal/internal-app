from django.contrib.auth import authenticate, login 
from django.contrib.auth.views import logout_then_login, password_change
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from profiles.models import TeamMember
from feedbacks.models import Feedback
from forms import BadgeForm
from models import Badge

@login_required
def profile(request, id):
    person = TeamMember.objects.get(pk=id)
    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        if form.is_valid():
            b = Badge(badge_name=form.cleaned_data['name'], description=form.cleaned_data['description'], badge_image=form.cleaned_data['image'])
            b.save()
            person.badge.add(b)
            person.save()
    upload_form = BadgeForm()
    return render(request,'profiles/profile_base.html', {'person': person,
                                                        'avg': person.feedback_averages(), 'form': upload_form})

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

# Note, all user defined functions about password change start with 'change_pw', whereas django's
# begin with password_change
@login_required
def change_pw(request):
    return password_change(request, template_name='profiles/change_pw.html', post_change_redirect='/') 
    # Todo: Pranav - need to alert the user that password has been changed successfully with the messages framework.
def logout(request):
    return logout_then_login(request)
