from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def index(request):
    return render(request, 'authentication/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['confirm_password']
            User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email, password=password)
            messages.success(request, "User created.")
            return redirect('signin')
        else:
            messages.error(request, "User not created.")
    else:
        form = SignUp()
    return render(request, 'authentication/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request, 'authentication/index.html', {'fname': fname})
            else:
                messages.error(request, "Bad Credentials!")
                return redirect('index')
        else:
            form = SignIn()
    return render(request, 'authentication/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('index')
