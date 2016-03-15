from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")
    template = loader.get_template('video/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
