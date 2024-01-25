from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

# this function handles the signin credentials to provide user authetentication

def signin(request):
    # if method is post and has sended data Authenticating the user and logging
    if request.method == "POST":
        # Getting sent post or posted data
        _username = request.POST.get("username")
        _password = request.POST.get("password")

        user = authenticate(request, username=_username, password=_password)
        if user:
            login(request, user=user)
            return redirect("index")
        # invalid inputs
        else:
            messages.error(request, "Invalid user name or password")
            return redirect("signin")
    # when method is to get the signin page
    else:
        return render(request, "signin.html")
    
# this function handles the signin credentials to provide user authetentication
def register(request):
    if request.method == "POST":
        return redirect("index")
    else:
        return render(request, "register.html")

# this function handles the signin credentials to provide user authetentication
def index(request):
    if request.user.is_authenticated:
        context = {"context": f"Welome {request.user.username}"}
        return render(request, 'index.html', context)
    return render(request, 'index.html', {})