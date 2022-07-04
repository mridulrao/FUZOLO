
from django.shortcuts import render, redirect, get_object_or_404
from .models import product

from django.core.mail import send_mail


def event_page(request):
    products = product.objects
    
    return render (request, 'event_page/event_page.html', {'products':products})

def product_details(request, product_id):
    product_details = get_object_or_404(product,pk=product_id)
    return render(request,'event_page/product_details.html',{'product':product_details})

def product_form(request, product_id):
    product_details = get_object_or_404(product,pk=product_id)

    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        mail_list = []
        mail_list.append('clubfuzolo@gmail.com')
        title = 'Someone tried to contact you through website regarding ' + str(product_details)
        send_mail(title, str(message) + "\nEmail - " + str(email) , '', mail_list)
        return redirect('message-sent')

    return render(request,'event_page/product_form.html',{'product':product_details})

def messagesent(request):
    return render(request, 'event_page/messagesent.html')