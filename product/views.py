from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from product.forms import CommentForm
from product.models import Product, Comment


# Create your views here.


def product_list(request):
    products = Product.objects.order_by('-pub_date')

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product/product_list.html', {'page_obj': page_obj})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = product.comments.all()
    form = CommentForm()
    return render(request, 'product/product_detail.html', {
        'product': product,
        'comments': comments,
        'form': form
    })


@login_required
def comment_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.content_list = product
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()


@login_required
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.author:
        return redirect('product_detail', product_id=comment.content_list.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'product/comment_form.html', {'form': form, 'comment': comment})


@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author:
        comment.delete()

    return redirect('product_detail', product_id=comment.content_list.id)