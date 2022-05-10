from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import ClientForm, ObjectForm, ServiceForm, BookingForm
from .models import Client, Object, Service, Booking

@login_required
def client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
        client.self = client
        client.save()
        return redirect('chess:all_clients')
    context = {
        'form': form
    }
    return render(request, 'chess_spreadsheet/create_client.html', context)


@login_required
def object(request):
    form = ObjectForm(request.POST or None)
    if form.is_valid():
        object = form.save(commit=False)
        object.save()
        object.self = object
        object.save()
        return redirect('chess:all_objects')
    context = {
        'form': form
    }
    return render(request, 'chess_spreadsheet/create_object.html', context)


@login_required
def service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        service = form.save(commit=False)
        service.save()
        service.self = service
        service.save()
        return redirect('chess:all_services')
    context = {
        'form': form
    }
    return render(request, 'chess_spreadsheet/create_service.html', context)


@login_required
def booking(request):
    # context = {
    #     'clients': Client.objects.all(),
    #     'objects': Object.objects.all(),
    #     'services': Service.objects.all()
    # }
    # return render(request, 'chess_spreadsheet/create_booking.html', context)
    form = BookingForm(request.POST or None)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.save()
        booking.self = booking
        booking.save()
        return redirect('chess:all_bookings')
    context = {
        'form': form
    }
    return render(request, 'chess_spreadsheet/create_booking.html', context)
