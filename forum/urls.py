from django.urls import path, include
from django.conf.urls import url
from . import views #
from .views import PostCreateView, PostUpdateView, PostDeleteView, postdetail, upvote
from froala_editor.fields import FroalaField
from django.views.generic.base import RedirectView



urlpatterns = [
    path('', views.home, name = 'forum-home'),  #route, views
    path('about/', views.about, name='forum-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', views.postdetail, name='post-detail'),
    url(r'^froala_editor/', include('froala_editor.urls')),
    path('post/<int:pk>/', views.upvote, name='upvote'),
    
]

#PostDetailView.as_view()
#CommentCreateView.as_view()
#urls.py maps the url to the views function.  
