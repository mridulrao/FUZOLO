from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager



# Create your models here.
class FuzoloUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length = 255)

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    phone_number = PhoneNumberField()
    points = models.IntegerField(default = 0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email