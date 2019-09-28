from django import forms 
from .models import Post


class PostCreate(forms.ModelForm):
  
    

    class Meta:
        model = Post
        fields = ['title', 'content']
        

#import Post from the models file
#Import django's forms class.

#The PostCreate() class represents the model form
#Meta defins the model that needs to be used when creating the model form.
