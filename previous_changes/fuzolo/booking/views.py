from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Events, GetBooking

@csrf_exempt 
def product_details(request, product_name):
    product_details = get_object_or_404(Events,name=product_name)
    return render(request,'booking/product_details.html',{'product':product_details})

class booking_details():
    date = ''

selected_sport_dict  = {}
@csrf_exempt
def sport(request):
    if request.method == 'POST':
        if 'sport' in request.POST:
            booking_details.date = ''
            total_booked_slots.clear()
            title = request.POST['sport']
            #print(title)
            selected_sport  = Events.objects.filter(name = title)
            dict1 = {
            'title' : selected_sport[0].name,
            'content' : selected_sport[0].content
            }
            selected_sport_dict.clear()
            selected_sport_dict['title'] = selected_sport[0].title
            selected_sport_dict['content'] = selected_sport[0].content
        elif 'date' in request.POST:
            date = request.POST['date']
            booking_details.date = date
            dict1 = selected_sport_dict
    else:
        return redirect('events-page')

    #print(dict1)
    return render(request, 'booking/sport.html', {'dict':dict1})

final_slots = []
total_booked_slots = []
@csrf_exempt 
def booking_slots(request):
    if request.method == 'POST':
        date = booking_details.date
        date_converted = date[6:] + str('-') + date[0:2] + str('-') + date[3:5] 
        booked_slots = GetBooking.objects.filter(date = date_converted)
        total_booked_slots.clear()
        for i in range(len(booked_slots)):
            total_booked_slots.append(booked_slots[i].slots)
        dict2 = {
            'slots' : total_booked_slots
        }
        if 'Selected_Slots[]' in request.POST:
            req = request.POST
            selected_slots = req.getlist('Selected_Slots[]')
            final_slots.clear()
            final_slots.append(selected_slots)
        else:
            print("No DATA")
    else:
        date = booking_details.date
        if date != '--' and date != '':
            date_converted = date[6:] + str('-') + date[0:2] + str('-') + date[3:5] 
            booked_slots = GetBooking.objects.filter(date = date_converted)
            total_booked_slots.clear()
            for i in range(len(booked_slots)):
                total_booked_slots.append(booked_slots[i].slots)
        dict2 = {
            'slots' : total_booked_slots
        }
    return render(request, 'booking/booking_slots.html', {'slots':dict2})

@login_required
def booking_confirm(request):
    if request.user.is_authenticated:
        print(final_slots)
    return render(request, 'booking/booking_confirm.html')


def select_date(request):
    return render(request, 'booking/select_date.html')

