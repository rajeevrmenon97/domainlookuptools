"""nettools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import django.contrib.auth.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home',),
    url(r'^getall', views.getall, name = 'getall',),
    url(r'^whois/', include('whoisrec.urls', namespace = 'whoisrec')),
    url(r'^mx/', include('mx.urls', namespace = 'mx')),
    url(r'^aaaa/', include('aaaa.urls', namespace = 'aaaa')),
    url(r'^a/', include('a.urls', namespace = 'a')),
    url(r'^blacklist/', include('blacklist.urls', namespace = 'blacklist')),
    url(r'^ptr/', include('ptr.urls', namespace = 'ptr')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
] + staticfiles_urlpatterns()
