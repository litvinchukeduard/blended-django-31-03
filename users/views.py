from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect(to='cinema_app:index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_app:index')
        else:
            return render(request, 'users/register.html', {'form': form})
    return render(request, 'users/register.html', {'form': RegisterForm()})

def login_user(request):
    if request.user.is_authenticated:
        return redirect(to='cinema_app:index')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='cinema_app:index')

    return render(request, 'users/login.html', context={"form": LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='cinema_app:index')
