from datetime import datetime

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Object, Booking


@login_required
def employee_window(request):
    context = {
        'bookings': Booking.objects.all()
    }
    return render(request, 'chess_spreadsheet/employee_window.html', context)


def __get_hour(time):
    return datetime.strptime(time.strftime('%H'), '%H').hour


def __time_difference(time_from, time_to):
    return __get_hour(time_to) - __get_hour(time_from) + 1


@login_required
def chess(request, date):
    date = datetime.strptime(date, '%Y-%m-%d').date()
    bookings = Booking.objects.filter(date=date)

    context = {
        'time': [i for i in range(24)],
        'date': date,
        'bookings': [{
            'time': __get_hour(element.time_from),
            'hours_count': __time_difference(
                element.time_from,
                element.time_to
            ),
            'booking': element,
        } for element in bookings],
        'objects': Object.objects.filter(booking__in=bookings)
    }
    return render(request, 'chess_spreadsheet/chess.html', context)


@login_required
def chess_today(request):
    return redirect(reverse(
        'chess:chess',
        args=[datetime.today().strftime('%Y-%m-%d')]
    ))

# supervisor djf-ysq-8FX-EvD