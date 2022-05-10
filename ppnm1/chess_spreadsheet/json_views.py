from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Object, Client, Service, Booking


@login_required
def set_booking_status(request):
    booking = Booking.objects.get(pk=request.GET.get('booking_id'))
    booking.status = request.GET.get('value')
    booking.save()
    return JsonResponse({})


@login_required
def set_client(request):
    client = Client.objects.get(pk=request.GET.get('client_id'))
    client.name = request.GET.get('name')
    client.phone_number = request.GET.get('phone_number')
    client.email = request.GET.get('email')
    client.save()
    return JsonResponse({})


@login_required
def set_object(request):
    object = Object.objects.get(pk=request.GET.get('object_id'))
    object.title = request.GET.get('title')
    object.price = request.GET.get('price')
    object.description = request.GET.get('description')
    object.save()
    return JsonResponse({})


@login_required
def set_service(request):
    service = Service.objects.get(pk=request.GET.get('service_id'))
    service.title = request.GET.get('title')
    service.price = request.GET.get('price')
    service.description = request.GET.get('description')
    service.save()
    return JsonResponse({})


@login_required
def set_booking(request):
    booking = Booking()
    booking.status = '1' # Новая бронь
    booking.client = get_object_or_404(Client, name=request.GET.get('client'))
    booking.customers_count = request.GET.get('customers_count')
    booking.object = get_object_or_404(
        Object,
        title=request.GET.get('object')
    )
    services = request.GET.get('services')
    for service_pk in services:
        print(service_pk)
        booking.services.add(get_object_or_404(Service, pk=service_pk))
    booking.date = request.GET.get('date')
    booking.time_from = request.GET.get('time_from')
    booking.time_to = request.GET.get('time_to')
    booking.pub_date = datetime.now()
    booking.save()
    booking.self = booking
    booking.save()
    return JsonResponse({})
