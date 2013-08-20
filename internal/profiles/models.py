import os

import urllib
import hashlib
from django.utils.safestring import mark_safe

from django.conf import settings
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from social_auth.models import UserSocialAuth

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

class Badges(models.Model):
    badge_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.badge_name)

class TeamMember(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = TeamMemberManager()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    website = models.URLField(max_length=200)
    bio = models.TextField(blank=True)
    badges = models.ManyToManyField(Badges)
    avatar = models.URLField(null=True)

    # profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    USERNAME_FIELD = 'email'


    def full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        if self.first_name == '' and self.last_name == '':
            return self.email
        else:
            return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def feedback_averages(self):
        from feedbacks.models import Feedback
        if Feedback.objects.filter(target_id=self.id).count():
            result = Feedback.objects.filter(target_id=self.id).aggregate(Avg('participation_rating'),
                                                                          Avg('contribution_rating'),
                                                                          Avg('communication_rating'),
                                                                          Avg('ease_of_working_together_rating'))
            result['overall_rating__avg'] = (result['participation_rating__avg']
                                             + result['contribution_rating__avg']
                                             + result['communication_rating__avg']
                                             + result['ease_of_working_together_rating__avg'])/4
            return result
        else:
            return None

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

    @staticmethod
    def _set_avatar_callback(sender, **kwargs):
        if kwargs['created']:
            user = kwargs['instance']
            if user.password == '!': # means user is created through django social auth
                avatar_url = UserSocialAuth.objects.filter(user=user)[0].extra_data['avatar']
                user.avatar = avatar_url
                user.save()

post_save.connect(TeamMember._set_avatar_callback, weak=False, sender=TeamMember, dispatch_uid='save_avatar')

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
