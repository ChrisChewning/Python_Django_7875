from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#inherits from UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User 
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
           # 'username' : forms.CharField(label='')
        }
        fields = ['username', 'email', 'password1', 'password2']


 #added email to the existing form here. default () is required=True
 #class Meta is a nested namespace. keeps configurations in one place. saves to User model. 
 #in class Meta we set what we want this form to interact with. model = user
 #fields is what will be shown on the form. order matters. 
 #form.save() saves it 
 # 
 #        