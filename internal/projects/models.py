from django.db import models
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    collaborators = models.OneToManyField(Collaborator)
	leader = models.ForeignKey(Leader)
	startDate = models.DateField(max_length=10)
    deadLine = models.DateField(max_length=10)
    toDoList = models.ForeignKey(Plan)
    website = models.URLField()	
    
	
class Collaborator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
	Description = models.CharField(max_length=100)
	#picture = models.URLField() //Low priority
	#Roles = models.OneToManyField(Role)
	website = models.URLField()	#github page or anything that showcases the collaborator's background
	#ProjectList = models.OneToManyField(Project)
	#def createProject(self, keyword):
	#def joinProject(self, keyword):
	#def leaveProject(self, keyword):	
	#def leaveFeedback //Low priority

	
class Leader(models.Model):
    name = models.ForeignKey(Collaborator)
	project =  models.OneToManyField(Project)
	#def createDeadline(self, keyword):
	#def createTask(self, keyword):
	#def assignTask(self, keyword):
	#def killProject(self, keyword):
	
class Plan(models.Model):
    title = models.CharField(max_length=100)
	