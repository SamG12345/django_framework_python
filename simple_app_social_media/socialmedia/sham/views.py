from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth  import authenticate, login, logout
from .forms import CustomUserForm, LekhForm
from django.contrib import messages
from .models import Lekh, Profile
from django.http import JsonResponse

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
        form = LekhForm(request.POST or None)
        if form.is_valid():
            le = form.save(commit=False)
            le.profile = Profile.objects.get(user=request.user)
            le.save()
            return redirect("index")
        else:
            lekh = Lekh.objects.all().order_by('-date_created')
            return render(request, "pages/index.html", {"lekhs":lekh, "form":form})
    else:
        return redirect("signin")

# signout the user if logged in
def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("signin")

# profile viewing
def profile_view(request, id):
    if request.user.is_authenticated:
        form = LekhForm(request.POST or None)
        if form.is_valid():
            le = form.save(commit=False)
            le.profile = Profile.objects.get(user=request.user)
            le.save()
            return redirect("index")
        profile = get_object_or_404(Profile, id=id)
        print("profile = ",profile)
        lekhs = Lekh.objects.filter(profile=profile).order_by("-date_created")
        print("lekhs = ", lekhs)
        return render(request, 'pages/profile.html', {"profile":profile, "lekhs":lekhs, 'form':form})

# like_lekh
def like_lekh(request, lekh_id):
    if request.user.is_authenticated:
        lekh = get_object_or_404(Lekh, id=lekh_id)
        profile = get_object_or_404(Profile, user=request.user)
        response_data = {}
        if lekh.likes.filter(id=profile.id).exists():
            # If liked, remove the like
            lekh.likes.remove(profile)
            response_data = {'message': 'Unliked'}
        else:
            # If not liked, add the like
            lekh.likes.add(profile)
            response_data = {'message': 'Liked'}
        return JsonResponse(response_data)
    else:
        return redirect("signin")

# lekh_view
def lekh_view(request, lekh_id):
    if request.user.is_authenticated:
        lekh = get_object_or_404(Lekh, id=lekh_id)
        form = LekhForm(request.POST or None)
        if lekh:
            return render(request, "pages/lekh.html", {"lekh": lekh, 'form': form})
    else:
        return redirect("signin")