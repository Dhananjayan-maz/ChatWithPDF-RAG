from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import NumberInput, DateInput


User = get_user_model()

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
class SignInForm(AuthenticationForm):
    pass