from django.conf.urls import patterns, url

from Listener import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'response', views.text_test, name='response'),
)