from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
from django.shortcuts import loader

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from . import forms
from .models import Video
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")
    if request.user.is_authenticated():
        videos = Video.objects.all()
        #output = ', '.join([str(video) for video in videos])
        return render(request, 'video/index.html', {'videos': videos })
    else:
        return render(request, 'login_error.html')
    #template = loader.get_template('video/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))

def video_detail(request, pk):
    #video = Video.objects.get(pk=pk)

    video = get_object_or_404(Video, pk=pk)
    email = 'rhsu0268@gmail.com'
    return render(request, 'video/video_detail.html', {'video': video, 'email': email})

@login_required
def note_create(request, video_pk):
    video = get_object_or_404(Video, pk=video_pk)
    form = forms.NoteForm()

    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            # don't put this in the database
            note = form.save(commit=False)
            note.video = video
            note.save()
            messages.add_message(request, messages.SUCCESS, 'Note Added!')
            return HttpResponseRedirect(note.get_absolute_url())

    return render(request, 'video/note_form.html', {'form': form, 'video': video})
