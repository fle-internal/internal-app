import contextlib
import json
import urllib
import urllib2

from django.conf import settings
from django.dispatch import receiver

from github3 import login

from dashboard.models import News
from events.signals import github_issue_updated

@receiver(github_issue_updated) # can be a list of signals
def fetch_latest_github_events(sender, **kwargs):
    data = {'client_id': settings.GITHUB_APP_ID, 'client_secret': settings.GITHUB_API_SECRET}
    endpoint = kwargs['repo']['url'] + '/events'
    params = urllib.urlencode(data)
    full_url = endpoint + '?' + params
    with contextlib.closing(urllib2.urlopen(full_url)) as req:
        rawdata = req.read()
        events = json.loads(rawdata)
        return map(save_event, events)

def save_event(event):
    type = event['type']
    if type == 'IssuesEvent':
        return _save_issue_event(event)
    elif type == 'IssueCommentEvent':
        return _save_issue_comment_event(event)
    else:
        return None

def _save_issue_event(event):
    action = event['payload']['action']
    actor = event['actor']['login']
    url = event['payload']['issue']['html_url']
    issue_number = event['payload']['issue']['number']
    title = "{} {} issue #{}.".format(actor, action, issue_number)
    desc = "User {} has {} issue #{}.".format(actor, action, issue_number)
    return News.objects.create(title=title,
                               description=desc,
                               link=url,
                               type='IssuesEvent')

def _save_issue_comment_event(event):
    content = event['payload']['comment']['body']
    actor = event['actor']['login']
    issue_number = event['payload']['issue']['number']
    url = event['payload']['comment']['html_url']
    title = "@{} commented on issue #{}".format(actor, issue_number)
    desc = "User @{} commented on issue #{}: {}".format(actor,
                                                        issue_number,
                                                        content)
    return News.objects.create(title=title,
                               description=desc,
                               link=url,
                               type='IssueCommentEvent')
