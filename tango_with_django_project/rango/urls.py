from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url('^$', views.index),
        url(r'about', views.about))