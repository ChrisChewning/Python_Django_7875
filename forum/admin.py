from django.contrib import admin
from .models import Post, Comment

#register to show on Admin page. 
admin.site.register(Post) 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'content', 'approved')

admin.site.register(Comment, CommentAdmin)