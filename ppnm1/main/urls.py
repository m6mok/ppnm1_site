from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views


app_name = 'main'


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('book/<int:pk>/', views.book, name='book'),
	path('', views.index, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
