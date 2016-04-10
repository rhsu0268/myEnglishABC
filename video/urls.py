from django.conf.urls import url

from . import views

app_name = 'video'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'(?P<video_pk>\d+)/create_note/$', views.note_create, name='create_note'),
    url(r'(?P<pk>\d+)/$', views.video_detail, name='detail'),
]