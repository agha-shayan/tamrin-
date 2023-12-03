from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import post
from django.utils import timezone
#
# Create your views here.


def view1(request):
    return render(request, 'index.html')


def blog_home(request):
    current_time = timezone.now()
    posts = post.objects.filter(published_date__lte=current_time, status=1)
    context = {'postha': posts}

    return render(request, 'blog-home.html', context)


def blog_single(request):

    return render(request, 'blog-single.html',)


def detail(request, pk):
    current_time = timezone.now()
    posts1 =get_object_or_404(post,published_date__lte=current_time, status=1, id=pk)
    posts1.counted_view += 1
    posts1.save()
    context = {'postss': posts1}
    return render(request, 'blog-single.html', context)
