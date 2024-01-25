from django.urls import path
from . import views

urlpatterns = []

# url for acessing django login or signin page
urlpatterns += [path("signin", views.signin, name="signin"),]

# url for acessing django signup or registration page
urlpatterns += [path("register", views.register, name="register"),]

# url for acessing django index page after logging or signing
urlpatterns += [path("", views.index, name="index"),]