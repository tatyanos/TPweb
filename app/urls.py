from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>\d+)/like/$', views.like, name='like'),
    url(r'^add$', views.add, name='add'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^register$', views.register, name='register'),
    url(r'^search$', views.search, name='search'),
    url(r'^login$', views.login, name='login'),
)