from django.contrib.auth import get_user_model
from profiles import views
User = get_user_model()

def profile(request):
	return render(request,'profile.html', {'values': inhere}) #edit

def profile_index(request):
	return render(request,'profile_index.html') #edit
# Create your views here.

