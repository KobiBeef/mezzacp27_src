from django.conf.urls import patterns, url
from newtest00 import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
	)