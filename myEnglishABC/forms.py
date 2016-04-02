from django import forms
from django.core import validators


def must_be_empty(value):
	if value:
		raise forms.ValidationError('is not empty')

class SuggestionForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(validators=[must_be_empty])
	suggestion = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(10)])
	honeypot = forms.CharField(required=False, 
								widget=forms.HiddenInput, 
								label="Leave empty",
								validators=[validators.MaxLengthValidator(0)])
	# def clean_honeyput(self):
	# 	honeyput = self.cleaned_data['honeypot']
	# 	if len(honeypot):
	# 		raise forms.ValidationError(
	# 			"honeypot should be left empty. Bad bot!")
	# 	return honeypot

