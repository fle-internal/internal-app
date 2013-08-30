from django.dispatch import receiver

from events.signals import github_issue_updated
from profiles.models import TeamMember
from projects.models import Project, Task

@receiver(github_issue_updated)
def update_task_from_issue(issue, **kwargs):
    url = issue['html_url']
    try:
        task = Task.objects.get(github_link=url)
    except Task.DoesNotExist:
        task = Task()

    try:
        task.project = Project.objects.get(github_milestone_link=issue['milestone']['url'])
    except (Project.DoesNotExist, TypeError):
        pass

    try:
        task.assigned = TeamMember.objects.get(github_login=issue['assignee']['login'])
    except (TeamMember.DoesNotExist, TypeError):
        pass

    # the following attributes are the ones that are always set
    task.description = issue['title']
    task.github_link = url
    task.save()
    return task
