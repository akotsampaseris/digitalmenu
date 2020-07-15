from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User

from .forms import LoginForm, RegisterForm

# Create your views here.
def profile(request):
    users = User.objects.all()

    context = {
        "users": users
    }

    return render(request, 'users/profile.html', context)


def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(email=email)
            user.set_password(password)
            user.save()
            user.authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
            return redirect('users:profile')
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, 'users/register.html', context)


def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:profile')
            else:
                return HttpResponse('You have provided wrong credentials!')
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
