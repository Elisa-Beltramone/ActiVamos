from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'new_user.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)        
            return redirect('index')
        else:
            messages.success(request, ("There was an error."))
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    return render(request, 'index.html', {})