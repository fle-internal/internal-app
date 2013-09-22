from django.dispatch import Signal

# sent whenever an issue on github is opened, closed or commented on
github_issue_updated = Signal(providing_args=['issue', 'repo'])
