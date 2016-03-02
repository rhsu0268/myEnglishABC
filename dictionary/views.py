from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You are at the dictionary index.")

def detail(request, sentence_id):
	return HttpResponse("You are loking at sentence %s." % sentence_id)