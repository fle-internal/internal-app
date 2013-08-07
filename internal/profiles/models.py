import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class TeamMemberManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=TeamMemberManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class TeamMember(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = TeamMemberManager()

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    website = models.URLField(max_length=200)
    bio = models.TextField(blank=True)

    ###############################BADGES ADDED HERE ###############################################
    badges = models.ForeignKey(Badges)

    # profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    USERNAME_FIELD = 'email'

##############################BADGES ADDED HERE ###############################################
    def get_badges(self):
        return self.badges

    def full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        if self.first_name == '' and self.last_name == '':
            return self.email
        else:
            return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin

############### END OF TEAM MEMBER ##################################
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

############### BADGES TABLE ##################################
class Badges(models.Model):
    description = models.CharField(max_length=100)
    team_members = models.ManyToManyField(TeamMember)
