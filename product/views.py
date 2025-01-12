from django.shortcuts import render

from product.models import MainContent


# Create your views here.


def index(request):
    return render(request, 'product/product_list.html')
