from django.conf.urls import patterns, url
from test00 import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
	)