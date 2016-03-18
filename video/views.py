from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader

from .models import Video
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")

    videos = Video.objects.all()
    output = ', '.join([str(video) for video in videos])
    return HttpResponse(output)
    #template = loader.get_template('video/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))
