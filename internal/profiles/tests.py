"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from profiles.models import TeamMember
from projects.models import Project

class TeamMemberFeedback(TestCase):
    def setUp(self):
        self.t = TeamMember.objects.create(email='target@test.com', password='jollibee')
        self.m = TeamMember.objects.create(email='maker@test.com', password='jollibee')
        self.p = Project.objects.create(name='something', description='else', owner=self.t, start_date='2013-08-01', deadline='2014-08-01')
        self.t.feedbacks.create(maker=self.m,
                           project=self.p,
                           participation_rating=1,
                           contribution_rating=1,
                           communication_rating=1,
                           ease_of_working_together_rating=1)
        self.t.feedbacks.create(maker=self.m,
                           project=self.p,
                           participation_rating=3,
                           contribution_rating=3,
                           communication_rating=3,
                           ease_of_working_together_rating=3)

    def test_averaging(self):
        avgs = self.t.feedback_averages()
        self.assertEqual(avgs['participation_rating__avg'], 2, 'average is wrong')
        self.assertEqual(avgs['contribution_rating__avg'], 2, 'average is wrong')
        self.assertEqual(avgs['communication_rating__avg'], 2, 'average is wrong')
        self.assertEqual(avgs['ease_of_working_together_rating__avg'], 2, 'average is wrong')

    def test_averages_for_person_only(self):
        '''
        Averages should only count the feedbacks belonging to the team member
        '''
        self.m.feedbacks.create(maker=self.t,
                                project=self.p,
                                participation_rating=5,
                                contribution_rating=5,
                                communication_rating=5,
                                ease_of_working_together_rating=5)
        avgs = self.m.feedback_averages()
        self.assertEqual(avgs['participation_rating__avg'], 5, 'average is wrong')
        self.assertEqual(avgs['contribution_rating__avg'], 5, 'average is wrong')
        self.assertEqual(avgs['communication_rating__avg'], 5, 'average is wrong')
        self.assertEqual(avgs['ease_of_working_together_rating__avg'], 5, 'average is wrong')
