from django.db import models

class News(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    type = models.CharField(max_length=20)
    link = models.URLField(null=True, blank=True)
    date = models.DateField()

    @classmethod
    def recent(self):
        return self.objects.all()[:10]
