from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .forms import LoginForm, RegisterForm, EditUserForm

# Create your views here.@login_required
def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('dashboard:index')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, 'The passwords you provided do not match!')
                return redirect('users:register')

            try:
                user = form.save()
            except:
                return redirect('users:register', {"email": email})

            user.set_password(password)
            user.save()

            # Login user after registration
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome to DigitalMenu!')
                return redirect('dashboard:index')
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, 'users/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('dashboard:index')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'You have logged in successfully!')
                    return redirect('dashboard:index')
                else:
                    messages.error(request, 'Your account has been deactivated!')
                    return redirect('users:login')
            else:
                messages.error(request, 'The details you provided were wrong!')
                return redirect('users:login')
    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, 'users/login.html', context)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('pages:home')
