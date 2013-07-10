from django.db import models

class FLE(models.Model):
	name = models.CharField(max_length=30)
	# picture = models.??????
	badges = models.CharField(max_length=50) # this will surely change
	skills = models.CharField(max_length=100)
	links = models.CharField(max_length=100)
	projects = models.CharField(max_length=100)
	# perhaps this will be better later?
	# projects = models.ManyToManyField(Project)
	biography = models.CharField(max_length=500)
	email = models.EmailField()
