"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import copy
import datetime

from django.test import TestCase

from events.github import update_task_from_issue
from profiles.models import TeamMember
from projects.models import Task, Project

class TaskTestCase(TestCase):
    def setUp(self):
        self.data = {
            'html_url': 'github.com/barbero',
            'assignee': { 'login': 'aronasorman' },
            'milestone': { 'url': 'somewhere' },
            'title': 'fake issue',
        }

    def test_with_milestone_assigned_no_task_yet_task_created(self):
        self.assertFalse(Task.objects.filter(github_link=self.data['html_url']).exists())
        update_task_from_issue(self.data)
        Task.objects.get(github_link=self.data['html_url']) # raise error if not created

    def test_milestone_assigned(self):
        data_no_milestone = copy.copy(self.data)
        data_no_milestone['milestone'] = None
        update_task_from_issue(data_no_milestone)
        p = Project.objects.create(name='random project',
                                   owner_id=1,
                                   start_date=datetime.datetime.today(),
                                   deadline=datetime.datetime.today(),
                                   github_milestone_link=self.data['milestone']['url'],
        )
        update_task_from_issue(self.data)
        t = Task.objects.get(github_link=self.data['html_url'])
        self.assertEquals(t.project_id, p.id, "project was not assigned to task")

    def test_assignee_assigned(self):
        user = TeamMember.objects.create(
                email='fakeemail@hey.com',
                github_login='aronasorman',
                )
        t = update_task_from_issue(self.data)
        self.assertEquals(t.assigned_id, user.id, "user is not assigned")
