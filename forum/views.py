from django.shortcuts import render
from django.http import HttpResponse #


posts = [
    {
       'author': 'Chris',
        'title': 'Blog post 1', 
        'content': 'First post',
        'date_posted': 'Sept. 22, 2019'
    },
    {
        'author': 'Chris 2', 
        'title': 'Blog post 2',
        'content': 'Second post',
        'date_posted': 'Sept. 23, 2019'
    }
]


# Create your views here. handles traffic from home page of the forum.
def home(request):
    context = {
        'posts': posts #value is the posts []
    }
    return render(request, 'forum/home.html', context) #passes the data in here.
   
   
    #3rd optional arg is context. context is a dictionary here. the key is 'posts'. the value is a list of posts. 
    #was return HttpResponse('<h1>Forum Home</h1>'). it still returns that in the background.

def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})