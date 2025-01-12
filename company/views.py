from django.shortcuts import render

# Create your views here.


def history(request):
    return render(request, 'company/history.html')


def greeting(request):
    return render(request, 'company/greeting.html')


def location(request):
    return render(request, 'company/location.html')