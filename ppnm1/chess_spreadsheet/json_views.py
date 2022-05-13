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
    booking = get_object_or_404(Booking, pk=request.GET.get('booking_id'))
    booking.client = get_object_or_404(Client, pk=request.GET.get('client'))
    booking.customers_count = request.GET.get('customers_count')
    booking.object = get_object_or_404(
        Object,
        pk=request.GET.get('object')
    )
    booking.services.set([
        get_object_or_404(Service, pk=service_id)
        for service_id in request.GET.getlist('services[]')
    ])
    booking.date = request.GET.get('date')
    booking.time_from = request.GET.get('time_from')
    booking.time_to = request.GET.get('time_to')
    booking.save()
    booking.self = booking
    booking.save()
    return JsonResponse({})
