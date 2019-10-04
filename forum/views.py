from django.shortcuts import render, redirect
from django.http import HttpResponse #
from django import forms
from .models import Post, Comment
from .forms import PostCreate, CommentCreate   #. b.c it's in same directory. Post class
from django.views.generic import DetailView, CreateView, UpdateView
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor
from urllib.parse import urlsplit
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

#fn-based view
def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')[:10],
    }
    return render(request, 'forum/home.html', context) #passes the data in here.


#can't use decorators on classes. so login-mixin instead. 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    content = forms.CharField(widget=FroalaEditor)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    comment = CommentCreate(request.POST)
    comment.save()
    # if request.method == 'POST':
    #     form = CommentCreate(request.POST) #create a new form w data in request.POST
    #     if form.is_valid(): #bulit in to module. 
    #         form.instance.post = post
    #         username = form.cleaned_data.get('username')
    #         form.save()
    #     else:
    #         return redirect('login')
            
   
                
           
            
            
             #otherwise you get Integrity error: NOT NULL constraint failed: forum_comment.post_id
    # comment_form = CommentCreate(request.POST or None)
    #throwing the error

    # comment = Comment.objects.get(pk=pk)

    def form_valid(self, form):
        form.instance.post = post
        return super().form_valid(form)


    context = {
        'post': post,
        'content' : content,
        # 'object.author': Post.author,
        # 'comment': comment,
    }


    return render(request, "forum/post_detail.html", context)


class CommentCreateView(CreateView):
    template_name = 'forum/post_detail.html'
    model = Comment
    fields = ['content']
    content = forms.CharField(widget=FroalaEditor)



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)








#template has to be forum/post_form.html
#without form.instance.author..  you get the integrity error b.c author is NULL
#2nd error: no redirect. go to forum/models.py post model




def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})


#home is R (Read). Gets all the posts. 
#upload is C (Create). uploading form 

# Create your views here. handles traffic from home page of the forum.
