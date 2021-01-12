from django.contrib import admin
from django.urls import path, include
from .import views
from .views import *
from django.conf import settings


app_name = 'contact'
urlpatterns = [
        path('', PivotoraIndex.as_view() , name="index"),        
]