from django.shortcuts import render
from django.http import HttpResponse #
from .models import Post   #. b.c it's in same directory. Post class


# Create your views here. handles traffic from home page of the forum.
def home(request):
    context = {
        'posts': Post.objects.all()[:10]
    }
    return render(request, 'forum/home.html', context) #passes the data in here.
   
   
def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})