from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^page(?P<page_index>\d+)/$', views.index_page, name='index_page'),

    url(r'^ask/$', views.ask, name='ask'),
    url(r'^ask/add$', views.ask_add, name='ask_add'),

    url(r'^question/(?P<question_id>\d+)/$', views.question, name='question'),
    url(r'^question/(?P<question_id>\d+)/answer$', views.answer, name='answer'),
    url(r'^question/(?P<question_id>\d+)/like$', views.like, name='like'),


    url(r'^settings$', views.settings, name='settings'),
    url(r'^register$', views.register, name='register'),
    url(r'^search$', views.search, name='search'),

    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'app/login.html'}),
    url(r'^login$', views.login, name='login'),
)