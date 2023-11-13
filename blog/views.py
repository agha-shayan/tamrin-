from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    return render(request,'index.html')
def blog_home(request):
    return render(request,'blog-home.html')
def blog_single(request):
    return render(request,'blog-single.html')