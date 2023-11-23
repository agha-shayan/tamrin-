from django.shortcuts import render
from django.http import HttpResponse
from blog.models import post
from django.utils import timezone

# Create your views here.
def view1(request):
    return render(request,'index.html')

        
def blog_home(request):
    current_time=timezone.now()
    posts=post.objects.filter(published_date__lte=current_time)
    context={'postha':posts}

    
    return render(request,'blog-home.html',context)
    
def blog_single(request):

    return render(request,'blog-single.html',)
def detail(request,pk):
    posts1=post.objects.get(id=pk)
    posts1.counted_view+=1
    posts1.save()
    context={'postss':posts1}
    return render(request,'blog-single.html',context)