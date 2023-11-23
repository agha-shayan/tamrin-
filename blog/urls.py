from django.contrib import admin
from django.urls import path,include
from .views import *
app_name='blog'
urlpatterns = [
    
    path('',blog_home,name='blog_home'),
    path('blog_single',blog_single,name='blog_single'),
    #path('<int:age>',blog_home),
   # path('<str:name>',blog_single),
    path('blog/<int:pk>',detail),
    
]
