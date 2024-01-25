from django.urls import path
from . import views

# main index or home page
urlpatterns = [ path("", views.index, name="index"), ]

# signin page 
urlpatterns += [ path("signin", views.signin, name="signin"), ]


# registration
urlpatterns += [ path("signin", views.signin, name="signin"), ]