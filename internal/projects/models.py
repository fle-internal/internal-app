from django.db import models
from profiles.models import TeamMember
import datetime
from django.utils import timezone
# Create your models here.

    
class Task(models.Model):
    description = models.CharField(max_length=100)
    project = models.ForeignKey('Project', related_name='tasks')
    assigned = models.ForeignKey(TeamMember, related_name='tasks_assigned')
    deadline = models.DateField(blank=True, null=True)

    def __unicode__(self):
	   return self.title

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    owner = models.ForeignKey(TeamMember, related_name="projects_owned")
    collaborators = models.ManyToManyField(TeamMember, related_name="projects", through='Role')
    start_date = models.DateField(max_length=10)
    deadline = models.DateField(max_length=10)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Role(models.Model):
    profile = models.ForeignKey(TeamMember, related_name='roles')
    project = models.ForeignKey(Project)
    role_name = models.CharField(max_length=100)

    def __unicode__(self):
	   return self.role_name

