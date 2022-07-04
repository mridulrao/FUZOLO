from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'booking_slots/home.html')

def activity(request):
    return render(request, 'booking_slots/activity.html')

@csrf_exempt
def available_slots(request):
    if request.method == 'POST':
        print(request.POST)
        if 'Duration' in request.POST:
            duration = request.POST['Duration']
            print(duration)
        else:
            print("Not Found")
    return render(request, 'booking_slots/available_slots.html')

