from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^getfile', views.getfile, name = 'getfile'),
    url(r'^get', views.get, name = 'get'),
] + staticfiles_urlpatterns()
