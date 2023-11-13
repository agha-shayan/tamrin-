from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',view1),
    path('blog_home',blog_home),
    path('blog_single',blog_single)
]