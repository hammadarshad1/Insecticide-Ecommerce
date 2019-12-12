from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import *
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form1 = UserRegisterForm(request.POST)
        if form1.is_valid():
            form1.save()
            c = Profile(user = User.objects.all().last())
            c.save()
            messages.success(request, f'Your Account has been created! now you can login to your account')
            return redirect('Register')
        
    else:
        form1 = UserRegisterForm()

    return render(request,'users/register.html',{'form1':form1, 'title':'Register'})
    
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('Profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)