from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Client, Object, Service, Booking


@login_required
def objects(request):
    context = {
        'objects': Object.objects.all()
    }
    return render(request, 'chess_spreadsheet/all_objects.html', context)


@login_required
def clients(request):
    context = {
        'clients': Client.objects.all()
    }
    return render(request, 'chess_spreadsheet/all_clients.html', context)


@login_required
def bookings(request):
    context = {
        'bookings': Booking.objects.all()
    }
    return render(request, 'chess_spreadsheet/all_bookings.html', context)


@login_required
def services(request):
    context = {
        'services': Service.objects.all()
    }
    return render(request, 'chess_spreadsheet/all_services.html', context)
