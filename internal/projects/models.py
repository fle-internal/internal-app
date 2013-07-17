from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group

from profiles.models import TeamMember

class Project(Group):
	leader = models.ForeignKey(TeamMember, related_name='project_members')
	members = models.ManyToManyField(TeamMember)

	startDate = models.DateField(max_length=10)
	deadLine = models.DateField(max_length=10)
	#toDoList = models.ForeignKey(Plan)
	website = models.URLField()

	description = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name