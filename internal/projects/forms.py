from django.forms import *
from projects.models import *

class RoleForm(ModelForm):

    class Meta:
        model = Role
        widgets = { 'profile': HiddenInput,
                    'project': HiddenInput }

class ProjectForm(ModelForm):
    name = CharField(label='Project Name')
    class Meta:
        model = Project
        exclude = ("collaborators" , )
        widgets = { 'owner': HiddenInput }
