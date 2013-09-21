from datetime import datetime

from django.dispatch import receiver

from events.signals import github_issue_updated
from profiles.models import TeamMember
from projects.models import Project, Task

# wrapper function to the main worker function
@receiver(github_issue_updated)
def update_task(sender, **kwargs):
    issue = kwargs['issue']
    repo = kwargs['repo']
    return update_task_from_issue(issue, repo)

def update_task_from_issue(issue, repo):
    url = issue['html_url']
    try:
        task = Task.objects.get(github_link=url)
    except Task.DoesNotExist:
        task = Task()

    try:
        task.project = Project.objects.get(github_repo_link=repo['html_url'], name=issue['milestone']['title'])
    except (Project.DoesNotExist, TypeError):
        pass

    try:
        task.assigned = TeamMember.objects.get(github_login=issue['assignee']['login'])
    except (TeamMember.DoesNotExist, TypeError):
        pass

    # the following attributes are the ones that are always set
    task.description = issue['title']
    task.github_link = url
    task.status = issue['state']
    task.save()
    return task

def create_project_from_milestone(milestone, repo):
    due_on = datetime.strptime(milestone['due_on'], '%Y-%m-%dT%H:%M:%SZ').date()
    created_at = datetime.strptime(milestone['due_on'], '%Y-%m-%dT%H:%M:%SZ').date()
    return Project.objects.get_or_create(name=milestone['title'],
                                         github_repo_link=repo['html_url'],
                                         defaults={'description' : milestone['description'],
                                                   'deadline' : due_on,
                                                   'start_date' : created_at,
                                         }
    )
