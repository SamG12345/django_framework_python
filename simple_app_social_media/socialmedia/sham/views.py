from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login

# Create your views here.

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

