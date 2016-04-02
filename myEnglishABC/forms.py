from django import forms


class SuggestionForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	suggestion = forms.CharField(widget=forms.Textarea)
	honeypot = forms.CharField(required=False, 
								widget=forms.HiddenInput, 
								label="Leave empty")
	def clean_honeyput(self):
		honeyput = self.cleaned_data['honeypot']
		if len(honeypot):
			raise forms.ValidationError(
				"honeypot should be left empty. Bad bot!")
		return honeypot