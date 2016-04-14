from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from django.views.generic import View

#from .forms import SuggestionForm
from . import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def index(request):
    #return HttpResponse("Hello, world. You are at the homepage of the application")
   return render(request, 'index.html', {'time': datetime.now() })


# class login(View):

# 	def get(self, request, *args, **kwargs):
# 		return render(request, 'login.html')

# 	def post(request):
# 		return HttpResponse('This is POST request!')

def login(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/home")
    else:
        # Show an error page
        return render(request, "login/login.html")

def show_register(request):
	return render(request, 'register.html', {'time': datetime.now() })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})

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


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

def home(request):
	return render(request, 'home.html')