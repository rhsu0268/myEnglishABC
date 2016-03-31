from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

#from .forms import SuggestionForm
from . import forms

def index(request):
    #return HttpResponse("Hello, world. You are at the homepage of the application")
   return render(request, 'index.html', {'time': datetime.now() })

def suggestion_view(request):
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST)
		if form.is_valid():
			#print("good form")
			send_mail(
				'Suggestion from {}'.format(form.cleaned_data['name']),
				form.cleaned_data['suggestion'],
				'{name} <{email}>'.format(**form.cleaned_data),
				['rhsu@gwu.edu']
				)
			messages.add_message(request, messages.SUCCESS, 'Thanks for your suggestion!')
			return HttpResponseRedirect(reverse('suggestion'))
	return render(request, 'suggestion_form.html', {'form': form})