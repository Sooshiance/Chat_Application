from django.shortcuts import render, redirect
from django.contrib import auth 
from django.contrib.auth.models import User 

from .forms import Register


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('HOME')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('HOME')
        else:
            return render(request, 'login.html')
    return render(request, "user/login.html")        


def logoutUser(request):
    auth.logout(request=request)
    return redirect('HOME')


def registerUser(request):
    form = Register(request.POST)
    if request.user.is_authenticated:
        return redirect('HOME')
    elif request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 != password2:
                return redirect('REGISTER')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.set_password(password1)
                user.save()
            return redirect('HOME')
        else:
            return redirect('LOGIN')
    form = Register()
    return render(request, 'user/register.html', {'form':form})
