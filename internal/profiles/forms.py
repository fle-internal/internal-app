from django import forms

class BadgeForm(forms.Form):
	image = forms.ImageField()
	name = forms.CharField()
	description = forms.CharField(widget=forms.Textarea)



