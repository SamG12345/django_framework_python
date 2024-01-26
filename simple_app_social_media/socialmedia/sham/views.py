from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login
from .forms import CustomUserForm
from django.contrib import messages
from .models import Lekh

# Create your views here.

# user signin
def signin(request):
    # if data is posted to signin and goes through authentication
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # authenticating user to login
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Wrong cred")
            return redirect('signin')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'pages/signin.html')

# register user and create a profile
def register(request):
    # if data is posted to register and goes through validation and saved
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        # checking the form is valid to be saved
        if form.is_valid():
            form.save()
            messages.success(request, "registration successful")
            return render(request, 'pages/register.html', {})
        else:
            messages.error(request, "registration not successful")
            return redirect('register')
    
    else:
        if request.user.is_authenticated:
            return redirect('index')
        form = CustomUserForm()
        return render(request, 'pages/register.html', {"form": form})

# home or index page if user logged
def index(request):
    if request.user.is_authenticated:
        lekh = Lekh.objects.all().order_by('-date_created')
        return render(request, "pages/index.html", {"lekhs":lekh})
    else:
        return redirect("signin")
