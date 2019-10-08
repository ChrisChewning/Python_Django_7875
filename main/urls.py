from django.urls import path, include
from django.conf.urls import url
from . import views #
from .views import Breweries


#main/
urlpatterns = [
    path('', views.Breweries, name = 'breweries-home'),  #route, views    
        # path('post/new/', PostCreateView.as_view(), name='post-create'),

]

#PostDetailView.as_view()
#CommentCreateView.as_view()
#urls.py maps the url to the views function.  