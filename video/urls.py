from django.conf.urls import url

from . import views

app_name = 'video'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'(?P<pk>\d+)/$', views.video_detail, name='detail'),
]
