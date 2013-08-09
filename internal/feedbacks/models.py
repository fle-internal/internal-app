from django.db import models
from django.db.models import *

from profiles.models import TeamMember
from projects.models import Project

class Feedback(models.Model):
    RATING_CHOICES = zip(range(6), range(6)) # 0 - 5 scale of rating

    maker = models.ForeignKey(TeamMember, related_name='feedbacks_made')
    target = models.ForeignKey(TeamMember, related_name='feedbacks')
    project = models.ForeignKey(Project, related_name="feedbacks")
    participation_rating = models.IntegerField(choices=RATING_CHOICES)
    participation_rationale = models.TextField()
    contribution_rating = models.IntegerField(choices=RATING_CHOICES)
    contribution_rationale = models.TextField()
    communication_rating = models.IntegerField(choices=RATING_CHOICES)
    communication_rationale = models.TextField()
    ease_of_working_together_rating = models.IntegerField(choices=RATING_CHOICES)
    ease_of_working_together_rationale = models.TextField()

"""class Avg(Feedback):
    avg_participation = Feedback.objects.aggregate(Avg('participation_rating'))
    avg_contribution = Feedback.objects.aggregate(Avg('contribution_rating'))
    avg_communication = Feedback.objects.aggregate(Avg('communication_rating'))
    avg_ease = Feedback.objects.aggregate(Avg('ease_of_working_together_rating'))

    participation = avg_participation['participation_rating__avg']
    contribution = avg_contribution['contribution_rating__avg'] 
    communication = avg_communication['communication_rating__avg'] 
    ease = avg_ease['ease_of_working_together_rating__avg']

    avg_stars = ( participation
                + contribution
                + communication
                + ease)/4"""

