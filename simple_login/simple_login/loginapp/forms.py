from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creating User from acceptance
class CustomUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'passowrd1', 'password2']