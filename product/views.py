from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from product.models import Product


# Create your views here.


def product_list(request):
    products = Product.objects.order_by('-pub_date')

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product/product_list.html', {'page_obj': page_obj})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})
