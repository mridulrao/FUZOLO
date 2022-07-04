from django.db import models
from django.forms import ImageField
from fuzolo import settings

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to='images/', blank = True)

    img1 = models.ImageField(upload_to='images/', blank = True)
    txt1 = models.CharField(max_length = 200)

    img2 = models.ImageField(upload_to='images/', blank = True)
    txt2 = models.CharField(max_length = 200)

    img3 = models.ImageField(upload_to='images/', blank = True)
    txt3 = models.CharField(max_length = 200)

    extra_description = models.TextField()

    def __str__(self):
        return self.name

class GetBooking(models.Model):
    date = models.DateField()
    slots = models.CharField(max_length = 255)
    user = models.CharField(max_length = 255)

    def __str__(self):
        return self.slots

