from django.shortcuts import get_object_or_404, render
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


def video_detail(request, pk):
    #video = Video.objects.get(pk=pk)

    video = get_object_or_404(Video, pk=pk)
    email = 'rhsu0268@gmail.com'
    return render(request, 'video/video_detail.html', {'video': video, 'email': email})
