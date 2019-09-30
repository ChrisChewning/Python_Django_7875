from django import forms 
from .models import Post, Comment
from froala_editor.widgets import FroalaEditor

class PostCreate(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
             'content': forms.CharField(widget=FroalaEditor)
        }

class CommentCreate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
             'content': forms.CharField(widget=FroalaEditor)
        }

#import Post from the models file
#Import django's forms class.

#The PostCreate() class represents the model form
#Meta defins the model that needs to be used when creating the model form.
