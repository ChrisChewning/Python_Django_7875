from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#inherits from UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            #self.fields[fieldname].label = None

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
           # 'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
            'email' : forms.TextInput(attrs = {'placeholder': 'Email Address'}),
            'password1' : forms.TextInput(attrs = {'placeholder': 'Password'}),
            'password2' : forms.TextInput(attrs = {'placeholder': 'Confirm Password'}),
        }
   
   #https://stackoverflow.com/questions/13523286/how-to-add-placeholder-to-forms-of-django-registration


 #added email to the existing form here. default () is required=True
 #class Meta is a nested namespace. keeps configurations in one place. saves to User model. 
 #in class Meta we set what we want this form to interact with. model = user
 #fields is what will be shown on the form. order matters. 
 #form.save() saves it 
 # 
 #        

class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()

     class Meta:
         model = User
         fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



        #ModelForm = https://stackoverflow.com/questions/2303268/djangos-forms-form-vs-forms-modelform
        #class Meta takes in the model and what fields you want to work with.