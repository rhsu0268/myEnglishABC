"""myEnglishABC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

#from . import login


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', views.login),
    url(r'^home/', views.home),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^dictionary/', include('dictionary.urls', namespace='dictionary')),
    url(r'^video/', include('video.urls', namespace='video')),
    url(r'^suggest/$', views.suggestion_view, name='suggestion'),
    url(r'^contact/$', views.contact_view, name='contact'),
    url(r'^tutor/', include('tutor.urls', namespace='tutor')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()