import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from events.github import update_task_from_issue

@csrf_exempt
def github(request):
    data = json.loads(request.POST['payload'])
    if 'issue' in data.keys(): # either an issue or issue_comment event
        update_task_from_issue(data['issue'], data['repository'])
    return HttpResponse('handled')
