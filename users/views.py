from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


#register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #create a new form w data in request.POST
        if form.is_valid(): #bulit in to module. 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm() #get request if empty. 
    return render(request, 'users/register.html', {'form': form})

#profile view
@login_required     #decorator to disallow logged out user seeing profile pg.
def profile(request):
    return render(request, 'users/profile.html')



#return request object, users template
#value is the new instance of the user creation form. 

#messages.debug, .info, .success, .warning, .error

#form.cleaned_data.get(...) get the username 
