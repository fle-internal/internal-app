from django.forms import *
from projects.models import *
from datetime import date

class RoleForm(ModelForm):

    class Meta:
        model = Role
        widgets = { 'profile': HiddenInput,
                    'project': HiddenInput }

class ProjectForm(ModelForm):
    name = CharField(label='Project Name')

    class Meta:
        model = Project
        exclude = ("collaborators",)
        widgets = { 'owner': HiddenInput,
                    'deadline': TextInput(attrs={'class': 'datepicker'}),
                    'start_date': TextInput(attrs={'class': 'datepicker'}),
        }
