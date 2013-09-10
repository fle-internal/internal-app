from django.db import models
from profiles.models import TeamMember
import datetime
from django.utils import timezone
from django.forms import ModelForm
# Create your models here.


class Task(models.Model):
    description = models.CharField(max_length=100)
    project = models.ForeignKey('Project', related_name='tasks', null=True)
    assigned = models.ForeignKey(TeamMember, related_name='tasks_assigned', null=True)
    deadline = models.DateField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True, db_index=True)
    status = models.CharField(max_length=7, default='open')

    def __unicode__(self):
        return self.description

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    owner = models.ForeignKey(TeamMember, related_name="projects_owned", null=True)
    collaborators = models.ManyToManyField(TeamMember, related_name="projects", through='Role')
    start_date = models.DateField(max_length=10)
    deadline = models.DateField(max_length=10)
    website = models.URLField()
    github_repo_link = models.URLField(blank=True, null=True, db_index=True)

    class Meta:
        unique_together = ('name', 'github_repo_link')

    def __unicode__(self):
        return self.name

class Role(models.Model):
    profile = models.ForeignKey(TeamMember, related_name='roles')
    project = models.ForeignKey(Project)
    role_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.role_name
