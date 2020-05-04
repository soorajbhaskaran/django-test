from django import forms
from newapp.models import Userinfo
from django.core import validators
from django.contrib.auth.models import User


class UserInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


def check_url(value):
    if 'https//:' not in value:
        raise forms.ValidationError('Please enter https:// at the beginning')

class UserProfileInfo(forms.ModelForm):

    class Meta():
        model = Userinfo
        fields = ('profile_pic', 'portfolio_name')
