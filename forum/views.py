from django.shortcuts import render, redirect
from django.http import HttpResponse #
from django import forms
from .models import Post, Comment
from .forms import PostCreate, CommentCreate   #. b.c it's in same directory. Post class
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor
from urllib.parse import urlsplit
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404


#fn-based view
def home(request):
    
    context = {
        'posts': Post.objects.all().order_by('-date_posted')[:10],  
    }
    return render(request, 'forum/home.html', context) #passes the data in here.


def upvote(request, pk):
    post = get_object_or_404(Post, pk=pk)
    already_liked = False
    
    if post.vote.filter(pk=request.user.pk).exists():
        post.vote.remove(request.user)
        already_liked = False
    else: 
        post.vote.add(request.user)
        already_liked = True


    context = {
        'post': post,
    }
    return render(request, "forum/post_detail.html", context)



#can't use decorators on classes. so login-mixin instead. 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    content = forms.CharField(widget=FroalaEditor)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#both needs to be to the left of UpdateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #get the post you want to update. check if logged in user == author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



    



def postdetail(request, pk):
    comment_form = CommentCreate()
    post = Post.objects.get(pk=pk)
    already_liked = False
    
    if post.vote.filter(pk=request.user.pk).exists():
        already_liked = True
    

    if request.method == 'POST':
        form = CommentCreate(request.POST) #create a new form w data in request.POST
       #user is authenticated needed
        if request.user.is_authenticated:
            username = request.user.username
        if form.is_valid(): #bulit in to module. 
            form.instance.post = post
            author = request.user.username
            form.save()
        else:
            return redirect('/')
            
  
# def article_new_comment(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.article = article
#             comment.created_date=timezone.now()
#             comment.save()
#             return redirect(article_detail, pk=article.pk)
#     else:
#         form=CommentForm()
#     return render(request, 'comments/add_new_comment.html', {'form': form})
            
            
             #otherwise you get Integrity error: NOT NULL constraint failed: forum_comment.post_id
    # comment_form = CommentCreate(request.POST or None)
    #throwing the error

    # comment = Comment.objects.get(pk=pk)

    def form_valid(self, form):
        form.instance.post = post
        return super().form_valid(form)


    context = {
        'post': post,
        'comment_form' : comment_form,
        'already_liked': already_liked,
        'total_likes': post.total_likes(),	
		}
        
    return render(request, "forum/post_detail.html", context)
  
   




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
