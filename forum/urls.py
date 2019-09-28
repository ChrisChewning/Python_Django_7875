from django.urls import path
from . import views #
from .views import PostDetailView, PostCreateView

urlpatterns = [
    path('', views.home, name = 'forum-home'),  #route, views
    path('about/', views.about, name='forum-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]



#urls.py maps the url to the views function.  