from django.shortcuts import render

from .models import GalleryImage


def index(request):
    return render(request, 'main/index.html')


def gallery(request):
    context = {
        'images': GalleryImage.objects.all()
    }
    return render(request, 'main/gallery.html', context)


def book(request, pk):
    return render(request, f'main/book_{pk}.html')
