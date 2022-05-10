from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403, handler400
from core.views import error_404, error_500


handler404 = error_404
handler500 = error_500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('chess/', include('chess_spreadsheet.urls', namespace='chess')),
	path('', include('main.urls', namespace='main')),
]
