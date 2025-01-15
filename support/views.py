from django.shortcuts import render

# Create your views here.


def notice(request):
    return render(request, 'support/notice.html')


def inquiry(request):
    return render(request, 'support/inquiry.html')
