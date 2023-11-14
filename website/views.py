from django.shortcuts import render

# Create your views here.
def view1(request):
    context={'text':'salammmmm',}
    return render(request,'index.html',context)