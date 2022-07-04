from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from booking import models
from django.views.generic import ListView

from users import models as user_model


def index(request):
    return render(request, 'fuzolo/index.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone_number = request.POST.get('phone_number')
        mail_list = []
        mail_list.append('clubfuzolo@gmail.com')
        title = 'Someone tried to contact you through website'
        send_mail(title, str(message) + "\nEmail - " + str(email) + "\nPhone Number - " + str(phone_number), '', mail_list)
        return redirect('message-sent')

    return render(request, 'fuzolo/contact.html')

def message_form(request):
    return render(request, 'fuzolo/message_sent.html')

def about(request):
    return render(request, 'fuzolo/about.html')

@login_required
def profile(request):
    if request.user.is_authenticated:
        email = request.user.email
        logged_user = get_object_or_404(user_model.FuzoloUser ,email = email)
        print(email)
    
    return render(request, 'fuzolo/profile.html', {'user': logged_user})

def events(request):
    sports = models.Events.objects.all()
    dict1 = {
        'sports' : sports
    }
    return render(request, 'fuzolo/events_new.html', {'events' : dict1})

