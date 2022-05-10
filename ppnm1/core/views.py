from django.shortcuts import render


def error_404(request, exception):
   context = {}
   return render(request, 'core/holder404.html', context)


def error_500(request):
   context = {}
   return render(request, 'core/holder500.html', context)
