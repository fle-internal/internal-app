from django import forms
from django.contrib import admin
from projects.models import Project
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

class ProjectAdminForm(forms.ModelForm):
    """A form for creating new projects. Includes all the required fields."""

    class Meta:
        model = Project
        fields = ('name', 'leader', 'deadLine')

    def save(self, commit=True):
        if commit:
            project.save()
        return project

class ProjectAdmin(GroupAdmin):
    # Standard things in ModelAdmin to exclude
    # Doesn't seem to work. Not sure what to do.
    #exclude = ('Permissions',)

    # The forms to add a project
    add_form = ProjectAdminForm

    # The fields to be used in displaying the Project model.
    list_display = ('name', 'leader','deadLine',)
    list_filter = ('deadLine',)
    fieldsets = (
        (None, {'fields': ('name','leader')}),
        ('Members', {'fields': ('members',)}),
        ('Important dates', {'fields': ('startDate','deadLine',)}),
        ('More info', {'fields': ('website',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'leader', 'startDate', 'deadLine')}
        ),
    )
    search_fields = ('name',)
    ordering = ('deadLine',)
    filter_horizontal = ()

admin.site.register(Project,ProjectAdmin)