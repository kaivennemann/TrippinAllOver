from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'booking/home.html')


def about(request):
    return render(request, 'booking/about.html')
