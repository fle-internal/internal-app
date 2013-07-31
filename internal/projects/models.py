from django.db import models
from profiles.models import TeamMember
# Create your models here.

class Plan(models.Model):
    title = models.CharField(max_length=100)

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(TeamMember, related_name="projects_owned")
    collaborators = models.ManyToManyField(TeamMember, related_name="projects", through='Role')
    startDate = models.DateField(max_length=10)
    deadLine = models.DateField(max_length=10)
    toDoList = models.ForeignKey('Plan')
    website = models.URLField()

class Role(models.Model):
    profile = models.ForeignKey(TeamMember)
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
