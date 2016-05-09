from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader
from dictionary.models import Sentence

import datetime
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")
    #template = loader.get_template('dictionary/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'dictionary/index.html')

def saveSentence(request):
	# if 'sentence' in request.GET and request.GET['sentence']:
	# 	sentence = request.GET['sentence']
	# 	print(sentence)
	# return render(request, 'dictionary/saved_sentence.html')
	# if 'sentence' in request.GET:
	# 	message = 'You want to translate: %r' % request.GET['sentence']
	# else:
	# 	message = 'You submitted an empty form.'
	# return HttpResponse(message)

	now = datetime.datetime.now()
	current_user = request.user


	sentence = Sentence(sentence_text="hello", pub_date=now, user=current_user)

	sentence.save()

	resp = "The sentence has been saved!"
	return HttpResponseRedirect('dictionary/saved_sentence.html')

def showWords(request):
	resp = "These are your saved words!"
	return render(request, 'dictionary/saved_sentence.html')

def detail(request, sentence_id):
	return HttpResponse("You are loking at sentence %s." % sentence_id)