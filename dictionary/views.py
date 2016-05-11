from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
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
	return render(request, 'dictionary/saved_sentence.html')
	#return HttpResponseRedirect('dictionary/saveSentence')

def showWords(request):
	resp = "These are your saved words!"
	sentences = Sentence.objects.all()
	for sentence in sentences:
		# unicode_text = sentence.chinese_text.encode('unicode-escape')
		# print(unicode_text)
		sentence.chinese_text = sentence.chinese_text.encode('ascii').decode('unicode-escape')
		print(sentence.chinese_text)
	return render(request, 'dictionary/saved_sentence.html', { 'sentences': sentences })

def detail(request, sentence_id):
	return HttpResponse("You are loking at sentence %s." % sentence_id)

def saveWord(request):
    now = datetime.datetime.now()
    current_user = request.user
    resp = "The word has successfully been saved!"
    if request.is_ajax():
        if request.method == 'POST':
            chinese_text = request.POST.get('chinese_text')
            unicode_text = chinese_text.encode('unicode-escape')
            print(unicode_text)
            print(unicode_text.decode('unicode-escape'))
            sentence = Sentence(sentence_text=request.POST.get('text'), chinese_text=unicode_text, pub_date=now, user=current_user)
            sentence.save()
            return HttpResponse(resp)
