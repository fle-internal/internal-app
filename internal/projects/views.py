from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

#create project page which lets you assign the project name, members, and member positions
def create_project(request):
	return render(request, 'projects/create_project.html', {})

def project_index(request):
	username = 'User' #fix for later
	return render(request, 'projects/project_index.html', {'user_name': username})

def project_details(request):
	#variable values are placeholders for now
	title = "KA Lite"
	description = "Internal application for members within the org"
	active = True
	deadline = "September 1, 2013"
	leader = "Khan Academy"
	todo = ['project models', 'project details', 'profiles', 
		'profile details']
	team_members= {'Angelique':'Project details', 'Andres':'Project Models'}
	return render(request, 'projects/project_detail.html', {
			'project_title':title,
			'project_descrip':description,
			'active':active, 'deadline':deadline,
			'leader':leader, 'team_members':team_members,
			'todo':todo})
