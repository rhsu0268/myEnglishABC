from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader

from datetime import datetime

def index(request):
    #return HttpResponse("Hello, world. You are at the homepage of the application")
   return render(request, 'index.html', {'time': datetime.now() })