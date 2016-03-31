from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader

from datetime import datetime

#from .forms import SuggestionForm
from . import forms

def index(request):
    #return HttpResponse("Hello, world. You are at the homepage of the application")
   return render(request, 'index.html', {'time': datetime.now() })

def suggestion_view(request):
	form = forms.SuggestionForm()
	return render(request, 'suggestion_form.html', {'form': form})