from django.shortcuts import render
from django.http import HttpResponse #
from .models import Post   #. b.c it's in same directory. Post class


# Create your views here. handles traffic from home page of the forum.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'forum/home.html', context) #passes the data in here.
   
   
    #3rd optional arg is context. context is a dictionary here. the key is 'posts'. the value is a list of posts. 
    #was return HttpResponse('<h1>Forum Home</h1>'). it still returns that in the background.

def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})