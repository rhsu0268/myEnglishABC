from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You are at the dictionary index.")

    #videos = Video.objects.all()
    #output = ', '.join([str(video) for video in videos])
    return render(request, 'tutor/index.html')
    #template = loader.get_template('video/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))