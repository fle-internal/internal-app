from django.contrib import admin
from profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','links','skills','projects','biography')


admin.site.register(Profile, ProfileAdmin)


