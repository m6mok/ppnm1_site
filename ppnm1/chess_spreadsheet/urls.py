from django.urls import path

from . import views, json_views, all_views, detail_views, create_views


app_name = 'chess'


urlpatterns = [
    path('set_booking_status/', json_views.set_booking_status, name='set_booking_status'),
    path('set_client/', json_views.set_client, name='set_client'),
    path('set_object/', json_views.set_object, name='set_object'),
    path('set_service/', json_views.set_service, name='set_service'),
    path('set_booking/', json_views.set_booking, name='set_booking'),
    
    path('objects/', all_views.objects, name='all_objects'),
    path('clients/', all_views.clients, name='all_clients'),
    path('bookings/', all_views.bookings, name='all_bookings'),
    path('services/', all_views.services, name='all_services'),

    path('objects/<int:pk>/', detail_views.object, name='object_detail'),
    path('clients/<int:pk>/', detail_views.client, name='client_detail'),
    path('bookings/<int:pk>/', detail_views.booking, name='booking_detail'),
    path('services/<int:pk>/', detail_views.service, name='service_detail'),

    path('objects/create/', create_views.object, name='create_object'),
    path('clients/create/', create_views.client, name='create_client'),
    path('bookings/create/', create_views.booking, name='create_booking'),
    path('services/create/', create_views.service, name='create_service'),

    path('<str:date>/', views.chess, name='chess'),
	path('employee/', views.employee_window, name='employee'),

    path('', views.chess_today, name='chess_today')
]
