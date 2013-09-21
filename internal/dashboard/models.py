from django.db import models

class News(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    type = models.CharField(max_length=20)
