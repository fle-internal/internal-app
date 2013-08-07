from django import forms

from feedbacks.models import Feedback
from profiles.models import TeamMember

class FeedbackCreationForm(forms.Form):
    target = forms.ModelChoiceField(TeamMember.objects.none())
    participation_rating = forms.ChoiceField(widget=forms.RadioSelect,
                                             choices=Feedback.RATING_CHOICES)
    participation_rationale = forms.CharField(widget=forms.Textarea)
    contribution_rationale = forms.CharField(widget=forms.Textarea)
    communication_rationale = forms.CharField(widget=forms.Textarea)
    ease_of_working_together_rationale = forms.CharField(widget=forms.Textarea)
    contribution_rating = forms.ChoiceField(widget=forms.RadioSelect,
                                             choices=Feedback.RATING_CHOICES)
    communication_rating = forms.ChoiceField(widget=forms.RadioSelect,
                                             choices=Feedback.RATING_CHOICES)
    ease_of_working_together_rating = forms.ChoiceField(widget=forms.RadioSelect,
                                             choices=Feedback.RATING_CHOICES)
