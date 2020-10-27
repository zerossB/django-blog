from django import forms
from django.contrib.auth import forms as auth_forms

from .models import Social, User


class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ("linkedin", "facebook", "twitter")


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
