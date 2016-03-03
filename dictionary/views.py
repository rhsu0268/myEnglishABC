from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")
    template = loader.get_template('dictionary/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def detail(request, sentence_id):
	return HttpResponse("You are loking at sentence %s." % sentence_id)