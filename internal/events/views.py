import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from events.github import update_task_from_issue
from events.signals import github_issue_updated

@csrf_exempt
def github(request):
    data = json.loads(request.POST['payload'])
    if 'issue' in data.keys(): # either an issue or issue_comment event
        github_issue_updated.send(data, issue=data['issue'], repo=data['repository'])
    return HttpResponse('handled')
