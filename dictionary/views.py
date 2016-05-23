from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import loader
from dictionary.models import Sentence

import datetime
# Create your views here.


from gtts import gTTS
from tempfile import TemporaryFile
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from os.path import abspath, dirname
import random, string
#import pygame


def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")
    #template = loader.get_template('dictionary/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))
    if request.user.is_authenticated():
        return render(request, 'dictionary/index.html')
    else:
        return render(request, 'login_error.html')

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
    if request.user.is_authenticated():
    	resp = "These are your saved words!"
    	sentences = Sentence.objects.all()
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

def detail(request, sentence_id):
	return HttpResponse("You are loking at sentence %s." % sentence_id)

def saveWord(request):
    now = datetime.datetime.now()
    current_user = request.user
    resp = "The word has successfully been saved!"
    #if request.is_ajax():
    if request.method == 'POST':
        chinese_text = request.POST.get('chinese_text')
        unicode_text = chinese_text.encode('unicode-escape')
        #print(unicode_text)
        #print(unicode_text.decode('unicode-escape'))
        text = request.POST.get('text')
        #makeAudio(text)
        #print(abspath(dirname('hello.mp3')))
        #f = open('hello.mp3')
        #audio_file = File(f)

        # make a string for the filename
        id_string = makeId()
        #print(id_string)
        file_string = 'audio-' + id_string + '.mp3'
        #print(file_string)
        #tts = gTTS(text=text, lang='en')
        #tts.save(file_string)


        sentence = Sentence(sentence_text=request.POST.get('text'), chinese_text=unicode_text, audio_filename=file_string, pub_date=now, user=current_user)
        sentence.save()
        #sentence.text_recording.save('new', audio_file)
        #audio_fiel.close()

        #sentence.text_recording.save('test.mp3', f2, save=False)
        return HttpResponse(resp)
        #return HttpResponse(resp)

def makeAudio(text):
	tts = gTTS(text=text, lang='en')
	tts.save("hello-test.mp3")

def sayWord(request):
    resp="Say word"
    #return HttpResponse(resp)
    #if request.is_ajax():
    if request.method == 'POST':
        id = request.POST.get('id')
        word = Sentence.objects.get(pk=id)
        sentence = word.sentence
        return HttpResponse(sentence)
    #     return render(request, 'dictionary/saved_sentence.html')
    # #resp = "hello"
    return render(request, 'dictionary/saved_sentence.html')
    #return HttpResponse(resp)

def deleteWord(request, id):
    word = Sentence.objects.get(pk=id)

    # delete the word
    word.delete()

    # sentences = Sentence.objects.all()
    # for sentence in sentences:
    #     # unicode_text = sentence.chinese_text.encode('unicode-escape')
    #     # print(unicode_text)
    #     #sentence.chinese_text = sentence.chinese_text.encode('ascii').decode('unicode-escape')
    #     sentence.chinese_text = sentence.chinese_text.decode('unicode-escape')
    #     print(sentence.chinese_text)
    # return render(request, 'dictionary/saved_sentence.html', { 'sentences': sentences })
    return redirect("/dictionary/savedWords")

def makeId():

    length = 5
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])


