from django.shortcuts import render

def contact(request):
	return render(request, 'internal/contact.html', {})

def dashboard(request):
	#person = TeamMember.objects.get(pk=id)
	return render(request, 'internal/dashboard.html', {})