"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import copy
import datetime

from django.test import TestCase

from events.github import update_task_from_issue, create_project_from_milestone
from profiles.models import TeamMember
from projects.models import Task, Project

class TaskTestCase(TestCase):
    def setUp(self):
        self.data = {
            'html_url': 'github.com/barbero',
            'assignee': { 'login': 'aronasorman' },
            'milestone': { 'title': 'somewhere' },
            'title': 'fake issue',
            'state': 'open',
        }
        self.repo = {
                'html_url' : 'github.com/fakerepo',
        }

    def test_with_milestone_assigned_no_task_yet_task_created(self):
        self.assertFalse(Task.objects.filter(github_link=self.data['html_url']).exists())
        update_task_from_issue(self.data, self.repo)
        Task.objects.get(github_link=self.data['html_url']) # raise error if not created

    def test_milestone_assigned(self):
        empty_repo = None
        t = update_task_from_issue(self.data, empty_repo)
        self.assertEquals(t.project_id, None, "project has been assigned")
        p = Project.objects.create(name='somewhere',
                                   owner_id=1,
                                   start_date=datetime.datetime.today(),
                                   deadline=datetime.datetime.today(),
                                   github_repo_link=self.repo['html_url'],
        )
        update_task_from_issue(self.data, self.repo)
        t = Task.objects.get(github_link=self.data['html_url'])
        self.assertEquals(t.project_id, p.id, "project was not assigned to task")

    def test_assignee_assigned(self):
        user = TeamMember.objects.create(
                email='fakeemail@hey.com',
                github_login='aronasorman',
                )
        t = update_task_from_issue(self.data, self.repo)
        self.assertEquals(t.assigned_id, user.id, "user is not assigned")

    def test_milestones_with_same_repo_should_be_distinguished(self):
        p1 = Project.objects.create(name='project1',
                                    owner_id=1,
                                    start_date=datetime.datetime.today(),
                                    deadline=datetime.datetime.today(),
                                    github_repo_link=self.repo['html_url'],
        )
        p2 = Project.objects.create(name='somewhere',
                                    owner_id=1,
                                    start_date=datetime.datetime.today(),
                                    deadline=datetime.datetime.today(),
                                    github_repo_link=self.repo['html_url'],
        )
        t = update_task_from_issue(self.data, self.repo)
        self.assertEquals(t.project_id, p2.id, "the wrong project was assigned")

    def test_task_status_changes(self):
        t1 = update_task_from_issue(self.data, self.repo)
        self.assertEquals(t1.status, 'open', 'task status was not open')
        self.data['state'] = 'closed'
        t2 = update_task_from_issue(self.data, self.repo)
        self.assertEquals(t1.id, t2.id, 'not same object')
        self.assertEquals(t2.status, 'closed', 'task not closed')

class MilestoneTestCase(TestCase):

    def setUp(self):
        self.milestone = {'title': 'fake milestone',
                          'description': 'something',
                          'due_on': '2011-04-10T20:09:31Z',
                          'created_at': '2011-04-10T20:09:31Z' }
        self.repo = { 'html_url': 'somewhere' }

    def test_milestone_created(self):
        create_project_from_milestone(self.milestone, self.repo)
        Project.objects.get(name=self.milestone['title'], github_repo_link=self.repo['html_url'])
