"""fuzolo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import path

from .views import events, index, contact, profile, about, message_form
from users import views as users_view
from django.contrib.auth import views as auth_views
from booking import views as booking_views

# for images 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index-page'),
    path('contact/', contact, name = 'contact-page'),
    path('profile/', profile, name = 'profile-page'),
    path('about/', about, name = 'about-page'),
    path('sent_message/', message_form, name = 'message-sent'),
    path('register/', users_view.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('events/', events, name = 'events-page'),
    path('<product_name>/', booking_views.product_details, name = 'product_details'),
    path('select_date/', booking_views.select_date, name = 'select-date'),
    path('sport/', booking_views.sport, name = 'sport-view'),
    path('booking_slots/', booking_views.booking_slots, name = 'booking-slots'),
    path('booking_confirm/', booking_views.booking_confirm, name = 'booking-confirm'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
