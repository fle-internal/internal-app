from django.db import models
import datetime
# Create your models here.	
    
class Leader(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
	
class Collaborator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    #Description = models.CharField(max_length=100)
	#picture = models.URLField() //Low priority
	#Roles = models.OneToManyField(Role)
    #website = models.URLField()	#github page or anything that showcases the collaborator's background
	#ProjectList = models.OneToManyField(Project)
	#def createProject(self, keyword):
	#def joinProject(self, keyword):"""

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    collaborators = models.ManyToManyField(Collaborator)
    leader = models.ForeignKey(Leader)
    start_date = datetime.datetime.now()
    deadline = models.DateField(max_length=10)
    #toDoList = models.ForeignKey(Plan)
    website = models.URLField()

