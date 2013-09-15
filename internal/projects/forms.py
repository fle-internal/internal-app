from django.forms import *
from projects.models import *

class RoleForm(ModelForm):

    class Meta:
        model = Role
        widgets = { 'profile': HiddenInput,
                    'project': HiddenInput }
