from django.shortcuts import render, redirect
from django.http import HttpResponse #
from django import forms
from .models import Post
from .forms import PostCreate   #. b.c it's in same directory. Post class
from django.views.generic import DetailView, CreateView
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor


#fn-based view
def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')[:10],
    }
    return render(request, 'forum/home.html', context) #passes the data in here.
   
#class-based view. import from DetailView
class PostDetailView(DetailView):
    model = Post

#@login_required()
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    content = forms.CharField(widget=FroalaEditor)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
#template has to be forum/post_form.html
#without form.instance.author..  you get the integrity error b.c author is NULL
#2nd error: no redirect. go to forum/models.py post model


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

# Create your views here. handles traffic from home page of the forum.
