from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login
from .forms import CustomUserForm

# Create your views here.

# user signin
def signin(request):
    # if data is posted to signin and goes through authentication
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, login)
            return redirect('index')
    
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'signin.html')

# register user and create a profile
def register(request):
    # if data is posted to register and goes through validation and saved
    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form:
            form.save()
            return redirect('signup')
    
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'signup.html')
    
def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return redirect("signin")