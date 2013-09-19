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
    start_date = DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    deadline= DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = Project
        exclude = ("collaborators" , "start_date", "deadline")
        widgets = { 'owner': HiddenInput }
