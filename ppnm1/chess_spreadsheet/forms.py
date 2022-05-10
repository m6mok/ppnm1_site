from django.forms import ModelForm

from .models import Client, Object, Service, Booking


class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['self',]


class ObjectForm(ModelForm):
    class Meta:
        model = Object
        exclude = ['self']


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['self',]


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['self', 'status']
