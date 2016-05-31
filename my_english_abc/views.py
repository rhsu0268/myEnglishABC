from django.shortcuts import render

from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    #return HttpResponse("Hello, world. You are at the homepage of the application")
   return render(request, 'templates/index.html', {'time': datetime.now() })



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, new_user)
            return HttpResponseRedirect("/home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})


def login(request):
    if request.method == 'POST': 
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/home")
        else:
        	return render(request, "login/login.html")
    else:
        # Show an error page
        return render(request, "login/login.html")

def home(request):
    #print(request.user)
    fetchedUser = User.objects.get(pk=request.user.id)
    if fetchedUser is None:
        return render(request, 'home.html')
    else:
        return render(request, 'home.html', { 'fetchedUser': fetchedUser })

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")
  
def updateUser(request):
    # get the user
    user = User.objects.get(pk=request.user.id)
    print(user)
    if request.method == 'POST':
        user.first_name = request.POST['firstName']
        user.last_name = request.POST['lastName']
        user.save(update_fields=['first_name', 'last_name'])
        print(user.first_name)
        fetchedUser = getUpdatedUser(request)
        return HttpResponseRedirect('/home', {'fetchedUser': fetchedUser})

def getUpdatedUser(request):
    return User.objects.get(pk=request.user.id)
