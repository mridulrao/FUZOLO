from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import FuzoloUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = FuzoloUser
    list_display = ('email', 'is_staff', 'is_active','name', 'phone_number', 'points', 'date_joined')
    list_filter = ('email', 'is_staff', 'is_active','name', 'phone_number', 'points', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'phone_number', 'points', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','name')
    ordering = ('name','email')


admin.site.register(FuzoloUser, CustomUserAdmin)
