from django.contrib import admin

from .models import Client, Object, Service, Booking


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'email'
    )
    search_fields = ('name', 'phone_number',)
    empty_value_display = '-пусто-'


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'customers_count',
        'object',
        'date',
        'time_from',
        'time_to',
    )
    search_fields = (
        'client',
        'object',
        'date',
    )
    list_filter = ('client', 'date')
    empty_value_display = '-пусто-'


admin.site.register(Client, ClientAdmin)
admin.site.register(Object)
admin.site.register(Service)
admin.site.register(Booking, BookingAdmin)
