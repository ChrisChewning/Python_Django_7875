from django.urls import path, include
from django.conf.urls import url
from . import views #
from .views import PostDetailView, PostCreateView
from froala_editor.fields import FroalaField


urlpatterns = [
    path('', views.home, name = 'forum-home'),  #route, views
    path('about/', views.about, name='forum-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^froala_editor/', include('froala_editor.urls'))
]



#urls.py maps the url to the views function.  