from django.urls import path
from . import views

# main index or home page
urlpatterns = [ path("", views.index, name="index"), ]

# signin page 
urlpatterns += [ path("signin", views.signin, name="signin"), ]

# registration
urlpatterns += [ path("register", views.register, name="register"), ]

# logout
urlpatterns += [ path("signout", views.signout, name="signout"), ]

# profile
urlpatterns += [ path("profile/<int:id>", views.profile_view, name="profile"), ]