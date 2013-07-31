from django.db import models
from profiles.models import TeamMember
# Create your models here.

class Plan(models.Model):
    title = models.CharField(max_length=100)
    def __unicode__(self):
	return self.title

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    leader = models.ForeignKey(TeamMember, related_name="projects_led")
    collaborators = models.ManyToManyField(TeamMember, related_name="projects")
    startDate = models.DateField(max_length=10)
    deadLine = models.DateField(max_length=10)
    toDoList = models.ForeignKey('Plan')
    website = models.URLField()
    def __unicode__(self):
        return self.name

