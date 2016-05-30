from django.shortcuts import render

from dictionary.models import Sentence
from django.shortcuts import HttpResponse

import datetime


def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")
    #template = loader.get_template('dictionary/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'dictionary/index.html')



def saveWord(request):
    now = datetime.datetime.now()
    current_user = request.user
    resp = "The word has successfully been saved!"
    #if request.is_ajax():
    if request.method == 'POST':
        chinese_text = request.POST.get('chinese_text')
        unicode_text = chinese_text.encode('unicode-escape')
        text = request.POST.get('text')

        sentence = Sentence(sentence_text=request.POST.get('text'), chinese_text=unicode_text, pub_date=now, user=current_user)
        sentence.save()

        #sentence.text_recording.save('test.mp3', f2, save=False)
        return HttpResponse(resp)
        #return HttpResponse(resp)

def showWords(request):
    if request.user.is_authenticated():
    	resp = "These are your saved words!"
        current_user = request.user
    	sentences = Sentence.objects.filter(user=current_user)
    	for sentence in sentences:
    		# unicode_text = sentence.chinese_text.encode('unicode-escape')
    		# print(unicode_text)
            print(sentence)
    		#sentence.chinese_text = sentence.chinese_text.encode('utf8').decode('unicode-escape')
            sentence.chinese_text = sentence.chinese_text.decode('unicode-escape')
            #sentence.chinese_text = sentence.chinese_text.decode('unicode-escape')
    		#print(sentence.chinese_text)
    	return render(request, 'dictionary/saved_sentence.html', { 'sentences': sentences })
    else:
        return render(request, 'login_error.html')


def deleteWord(request, id):
    word = Sentence.objects.get(pk=id)

    # delete the word
    word.delete()

    current_user = request.user
    sentences = Sentence.objects.filter(user=current_user)
    for sentence in sentences:
		# unicode_text = sentence.chinese_text.encode('unicode-escape')
		# print(unicode_text)
        print(sentence)
		#sentence.chinese_text = sentence.chinese_text.encode('utf8').decode('unicode-escape')
        sentence.chinese_text = sentence.chinese_text.decode('unicode-escape')
        #sentence.chinese_text = sentence.chinese_text.decode('unicode-escape')
		#print(sentence.chinese_text)
    return render(request, 'dictionary/saved_sentence.html', { 'sentences': sentences })

def sayWord(request):
    resp="hello"
    #id = 19
    #return HttpResponse(resp)
    if request.method == 'POST':
        sentence_id = request.POST.get('sentence_id')
        #return HttpResponse(sentence_id)
        word = Sentence.objects.get(pk=sentence_id)
        return HttpResponse(word)
    return HttpResponse(resp)

