<<<<<<< HEAD
from django.contrib.auth import get_user_model
from profiles import views
User = get_user_model()

def profile(request):
	return render(request,'profile.html', {'values': inhere}) #edit

def profile_index(request):
	return redner(request,'profile_index.html') #edit
=======
# Create your views here.

>>>>>>> e70e803b9a4f1c29271b655ac1b73925e4013f9a
