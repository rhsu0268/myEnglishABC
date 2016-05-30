from django.conf.urls import url

from . import views

app_name = 'dictionary'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^saveWord/$', views.saveWord),
    url(r'^savedWords/$', views.showWords),
    url(r'^deleteWord/(?P<id>\d+)/$', views.deleteWord),
  	url(r'^sayWord/$', views.sayWord),
]