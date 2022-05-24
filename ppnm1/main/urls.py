from django.urls import path

from . import views


app_name = 'main'


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
	path('', views.index, name='index'),
]
