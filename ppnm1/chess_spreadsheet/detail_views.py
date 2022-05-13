from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Client, Object, Service, Booking


@login_required
def object(request, pk):
    object = get_object_or_404(Object, pk=pk)
    bookings = Booking.objects.filter(object=object)
    context = {
        'object': object,
        'bookings': bookings
    }
    return render(request, 'chess_spreadsheet/object_detail.html', context)


@login_required
def client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    bookings = Booking.objects.filter(client=client)
    context = {
        'client': client,
        'bookings': bookings
    }
    return render(request, 'chess_spreadsheet/client_detail.html', context)


@login_required
def booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    context = {
        'booking': booking,
        'booking_date': booking.self.date.strftime('%Y-%m-%d'),
        'booking_time_from': booking.self.time_from.strftime('%H:%M'),
        'booking_time_to': booking.self.time_to.strftime('%H:%M'),
        'booking_services':
            [service for service in booking.self.services.all()],
        'clients': Client.objects.all(),
        'objects': Object.objects.all(),
        'services': Service.objects.all()
    }
    return render(request, 'chess_spreadsheet/booking_detail.html', context)



@login_required
def service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    bookings = Booking.objects.filter(services__in=[service])
    context = {
        'service': service,
        'bookings': bookings
    }
    return render(request, 'chess_spreadsheet/service_detail.html', context)
