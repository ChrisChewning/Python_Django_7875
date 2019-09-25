from django.shortcuts import render, redirect
#don't need any more: from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #create a new form w data in request.POST
        for d in dir(form):
          print(d)
        if form.is_valid(): #bulit in to module. 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('forum-home')
    else:
        form = UserRegisterForm() #get request if empty. 
    return render(request, 'users/register.html', {'form': form})




#return request object, users template
#value is the new instance of the user creation form. 

#messages.debug, .info, .success, .warning, .error

#form.cleaned_data.get(...) get the username 
