from django.shortcuts import render, redirect
from django.http import HttpResponse #
from django import forms
from .models import Post
from .forms import PostCreate   #. b.c it's in same directory. Post class


# Create your views here. handles traffic from home page of the forum.
def home(request):
    context = {
        'posts': Post.objects.all()[:10]
    }
    return render(request, 'forum/home.html', context) #passes the data in here.
   

def createPost(request):
    return render(request, 'forum/post.html')


# def upload(request, template_name='forum/post.html'):
#     upload = PostCreate()
#     if request.method == 'POST':
#         upload = PostCreate(request.POST)
#         if upload.is_valid():
#             upload.save()
#             return redirect('forum/home')
    # else:
    #     return HttpResponse("your form is wrong")



def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})


#home is R (Read). Gets all the posts. 
#upload is C (Create). uploading form 