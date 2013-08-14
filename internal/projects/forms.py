from django.forms import *
from projects.models import *

class ProjectForm(ModelForm):
#name = CharField(label='Project Name')
	class Meta:
		model = Project
		exclude = ("collaborators" , )
		widgets = { 'owner': HiddenInput }
		
