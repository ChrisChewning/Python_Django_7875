from django.urls import path
from . import views #

urlpatterns = [
    path('', views.home, name = 'forum-home'),  #route, views
    path('about/', views.about, name='forum-about'),
    path('newpost/', views.createPost, name='newpost'),
]



#urls.py maps the url to the views function.  