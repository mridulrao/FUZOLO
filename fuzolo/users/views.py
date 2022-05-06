from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import CustomUserCreationForm, CustomUserChangeForm, FuzoloUserForm
from .models import FuzoloUser

import razorpay


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(email = form.cleaned_data['email'],
                                    password = form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('events-page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.user.is_authenticated:
        logged_email = request.user.email
        logged_user = FuzoloUser.objects.filter(email = logged_email)
        logged_user_dic = {
            'name' : logged_user[0].name,
            'email' : logged_user[0].email,
            'phone_number' : logged_user[0].phone_number,
            'points' : logged_user[0].points
        }
    return render(request, 'users/profile.html', {'user': logged_user_dic})