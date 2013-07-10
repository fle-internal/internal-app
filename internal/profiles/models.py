from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30,verbose_name='Last Name')
    email = models.EmailField(verbose_name='e-Mail')
    biography = models.TextField(verbose_name='About Me')
    links = models.URLField(verbose_name='Links To Projects Or Github')
    skills = models.TextField(verbose_name='Skills And Interests')
    projects = models.TextField()
    #photo = models.ImageField(verbose_name='your_Picture')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

