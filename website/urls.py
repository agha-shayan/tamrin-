from django.contrib import admin
from django.urls import path,include
from .views import *
app_name='website'
urlpatterns = [
    path('',view1,name='index'),

]