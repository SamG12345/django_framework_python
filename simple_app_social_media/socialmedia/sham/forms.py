from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']