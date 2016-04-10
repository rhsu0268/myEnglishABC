from django import forms

from . import models

class NoteForm(forms.ModelForm):
	class Meta:
		model = models.Note
		fields = [
			'note_title',
			'word_list',
			'video',
			'sentence_list',
		]


