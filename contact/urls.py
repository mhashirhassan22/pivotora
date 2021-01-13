from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from .import views
from .views import *
from django.conf import settings


app_name = 'contact'
urlpatterns = [
        path('', views.CalendarView.as_view() , name="index"),
        url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
        url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),  
]