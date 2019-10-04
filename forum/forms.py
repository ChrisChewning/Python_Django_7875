from django import forms 
from .models import Post, Comment
from froala_editor.widgets import FroalaEditor

#ModeLForm needs a model specified in class Meta
class PostCreate(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
             'content': forms.CharField(widget=FroalaEditor)
        }

class CommentCreate(forms.ModelForm):
    content = forms.CharField( label='')
    class Meta: 
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.CharField(widget=FroalaEditor)  
            # gets the error 'CharField' object has no attribute 'is_hidden'. I believe it has to be in a class CreateView, not a fn view. 
        }

  

#import Post from the models file
#Import django's forms class.

#The PostCreate() class represents the model form
#Meta defines the model that needs to be used when creating the model form.
