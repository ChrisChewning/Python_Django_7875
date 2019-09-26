from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
    if request.method == 'POST':
        #populates the form with the new info.
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #save
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Update complete!')
            return redirect('profile')
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context)
    
#passed into context so we can access the forms from our template.


#return request object, users template
#value is the new instance of the user creation form. 

#messages.debug, .info, .success, .warning, .error

#form.cleaned_data.get(...) get the username 
