from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Events, GetBooking
from users import models as user_model

from .time_dictionary import get_time

class BookingDetails:
    date = ''
    total_booked_slots = []
    final_slots = []
    game = ''
    user = ''
    total_amount = 0
    total_date = []
    total_start_time = []
    total_end_time = []
    points = 0


def get_next_date(date):
    date_parts = date.split("-")
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])

    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False

    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30

    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    if len(str(month)) == 1:
        converted_month = "0" + str(month)
    else:
        converted_month = str(month)

    if len(str(day)) == 1:
        converted_day = "0" + str(day)
    else:
        converted_day = str(day)



    next_day = str(year) + "-" + converted_month + "-" + converted_day
    return next_day



def min_max_date(date):
    if date < 50:
        return BookingDetails.date
    elif date >= 50 and date < 99:
        return get_next_date(BookingDetails.date)
    else:
        return get_next_date(get_next_date(BookingDetails.date))

def generate_final_bill(slots, date):
    start_time = []
    end_time = []
    date = []
    selected_slots = []
    for i in range(len(slots)):
        if i == 0:
            for num in slots[i]:
                selected_slots.append(int(num))
            if len(selected_slots) > 0:
                date.append(str(BookingDetails.date))
                start_time.append(str(get_time(min(selected_slots))))
                end_time.append(str(get_time(max(selected_slots))))
            selected_slots.clear()
        if i == 1:
            for num in slots[i]:
                selected_slots.append(int(num))
            if len(selected_slots) > 0:
                date.append(str(get_next_date(BookingDetails.date)))
                start_time.append(str(get_time(min(selected_slots))))
                end_time.append(str(get_time(max(selected_slots))))
            selected_slots.clear()
        if i == 2:
            for num in slots[i]:
                selected_slots.append(int(num))
            if len(selected_slots) > 0:
                date.append(str(get_next_date(get_next_date(BookingDetails.date))))
                start_time.append(str(get_time(min(selected_slots))))
                end_time.append(str(get_time(max(selected_slots))))
            selected_slots.clear()

    return date, start_time, end_time
    


#################################          SERVER CALSS      #####################################

@csrf_exempt 
def product_details(request, product_name):
    product_details = get_object_or_404(Events,name=product_name)
    BookingDetails.game = product_name
    return render(request,'booking/product_details.html',{'product':product_details})


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



@csrf_exempt
@login_required 
def booking_slots(request):
    #Ensure that there are not any pre-existing slots 
    BookingDetails.total_booked_slots.clear()
    if request.method == 'POST':
        BookingDetails.final_slots.clear()
        if 'Selected_Slots[0][]' in request.POST:
            selected_slots = request.POST.getlist('Selected_Slots[0][]')
            BookingDetails.final_slots.append(selected_slots)
        if 'Selected_Slots[1][]' in request.POST:
            selected_slots = request.POST.getlist('Selected_Slots[1][]')
            BookingDetails.final_slots.append(selected_slots)
        if 'Selected_Slots[2][]' in request.POST:
            selected_slots = request.POST.getlist('Selected_Slots[2][]')
            BookingDetails.final_slots.append(selected_slots)
        #BookingDetails.total_booked_time = get_total_time(BookingDetails.final_slots)
        if len(BookingDetails.final_slots) == 0:
            print("No Selected Slots")

        BookingDetails.total_date, BookingDetails.total_start_time, BookingDetails.total_end_time = generate_final_bill(BookingDetails.final_slots, BookingDetails.date)
    else:
        #Getting Date from book_game page 
       # print(BookingDetails.date)
        if BookingDetails.date != '':
            BookingDetails.total_booked_slots.clear()
            next_date = get_next_date(BookingDetails.date)
            next_next_date = get_next_date(next_date)
            booked_slots_today = GetBooking.objects.filter(date = BookingDetails.date)
            booked_slots_next_day = GetBooking.objects.filter(date = next_date)
            booked_slots_next_next_day = GetBooking.objects.filter(date = next_next_date)

            #Get Booked slots of that date, next_day, next_next_day
            booked_today = []
            for i in range(len(booked_slots_today)):
                booked_today.append(booked_slots_today[i].slots)
            
            booked_next_day = []
            for i in range(len(booked_slots_next_day)):
                booked_next_day.append(booked_slots_next_day[i].slots)

            booked_next_next_day = []
            for i in range(len(booked_slots_next_next_day)):
                booked_next_next_day.append(booked_slots_next_next_day[i].slots)


            BookingDetails.total_booked_slots.append(booked_today)
            BookingDetails.total_booked_slots.append(booked_next_day)
            BookingDetails.total_booked_slots.append(booked_next_next_day)

            #print(BookingDetails.total_booked_slots)

    
    dict_total_booked_slots = {
            'slots' : BookingDetails.total_booked_slots
        }

    return render(request, 'booking/booking_slots.html', {"slots" : dict_total_booked_slots})

@login_required
@csrf_exempt
def book_game(request):
    if request.method == 'POST':
        total_booked_slots = []
        if 'date' in request.POST:
            date_choosed = request.POST['date']
            BookingDetails.date = date_choosed
        else:
            print("No date found")

    return render(request, 'booking/book_game.html')

@login_required
def booking_confirm(request):
    BookingDetails.user = request.user.email
    user_info = user_model.FuzoloUser.objects.filter(email = BookingDetails.user)
    BookingDetails.points = user_info[0].points
    #BookingDetails.points = 
    context = {
        'user' : BookingDetails.user,
        'game' : BookingDetails.game,
        'Date' : BookingDetails.total_date,
        'Start_Time' : BookingDetails.total_start_time,
        'End_Time' : BookingDetails.total_end_time,
        'Points' : BookingDetails.points
    }

    return render(request, 'booking/booking_confirm.html', context)


def select_date(request):
    return render(request, 'booking/select_date.html')


