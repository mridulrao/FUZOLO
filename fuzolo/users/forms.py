from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FuzoloUser
from django import forms 


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = FuzoloUser
        fields = ['name', 'email', 'password1', 'phone_number']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = FuzoloUser
        fields = ('email',)


class FuzoloUserForm(forms.ModelForm):
    class Meta:
        model = FuzoloUser
        fields = ['name', 'email', 'password', 'phone_number']
        exclude = ['points', 'last_login', 'groups', 'user_permissions', 'is_superuser', 'is_staff', 'is_active', 'date_joined']