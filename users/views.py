from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView


# Create your views here.
def register(request):
    if request.method == "POST":
        form1 = forms.UserRegisterForm(request.POST)
        if form1.is_valid():
            form1.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! now you can login to your account')
            return redirect('Register')
        
    else:
        form1 = forms.UserRegisterForm()

    return render(request,'users/register.html',{'form1':form1, 'title':'Register'})


