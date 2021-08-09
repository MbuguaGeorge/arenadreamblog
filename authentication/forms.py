from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = "__all__"