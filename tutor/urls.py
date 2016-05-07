from django.conf.urls import url

from . import views

app_name = 'tutor'
urlpatterns = [

    url(r'^$', views.index, name='index'),
  
]