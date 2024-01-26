from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LekhForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder": "Write Something",
                                   "class": "form-control"
                               }
                           ),
                           label=""
                           )
