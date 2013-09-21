from django.db import models

class News(models.Model):
    TYPES = (('PUSH', 'push'),
             ('PULL_REQUEST', 'pull request'))

    title = models.CharField(max_length=25)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPES)
