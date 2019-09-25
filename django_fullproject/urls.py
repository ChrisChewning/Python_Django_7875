from django.contrib import admin
from django.urls import path, include 
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')), #now when we go to /forum it'll 
    path('register/', user_views.register, name='register')
]
