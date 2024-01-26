from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Lekh

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LekhForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder": "Write Something",
                                   "class": "form-control",
                                   "style": "resize: none; width: 400px; height: 100px;"

                               }
                           ),
                           label=""
                           )
    class Meta:
        model = Lekh
        fields=["body"]
