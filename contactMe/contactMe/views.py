from django.shortcuts import render, redirect
from django.core.mail import send_mail

def contactme(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        mail_list = []
        mail_list.append('clubfuzolo@gmail.com')
        send_mail('Someone tried to contact you through website!', str(message) + "\nEmail - " + str(email) , '', mail_list)
        return redirect('message-sent')
    return render(request, 'contactMe/contact.html')

def messagesent(request):
    return render(request, 'contactMe/messagesent.html')


def event_page(request):
    return render(request, 'contactMe/eventpage.html')
