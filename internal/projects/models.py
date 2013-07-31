from django.db import models
<<<<<<< HEAD
import datetime
# Create your models here.	
    
class Leader(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __unicode__(self):
        return self.first_name
	
class Collaborator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __unicode__(self):
        return self.first_name
    #Description = models.CharField(max_length=100)
	#picture = models.URLField() //Low priority
	#Roles = models.OneToManyField(Role)
    #website = models.URLField()	#github page or anything that showcases the collaborator's background
	#ProjectList = models.OneToManyField(Project)
	#def createProject(self, keyword):
	#def joinProject(self, keyword):"""
=======
from profiles.models import TeamMember
# Create your models here.

class Plan(models.Model):
    title = models.CharField(max_length=100)
>>>>>>> 00cdca17a23aca1a391b2e91407aef572037fcb0

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    leader = models.ForeignKey(TeamMember, related_name="projects_led")
    collaborators = models.ManyToManyField(TeamMember, related_name="projects")
    startDate = models.DateField(max_length=10)
    deadLine = models.DateField(max_length=10)
    toDoList = models.ForeignKey('Plan')
    website = models.URLField()
<<<<<<< HEAD
    def __unicode(self):
        return self.name

=======
>>>>>>> 00cdca17a23aca1a391b2e91407aef572037fcb0
