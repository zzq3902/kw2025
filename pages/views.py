from django.shortcuts import render

# Create your views here.


def home(request):
    # 가상 데이터 생성
    products = [
        {"name": "Product 1", "price": "10,000", "image": "/static/images/logo.jpg"},
        {"name": "Product 2", "price": "20,000", "image": "/static/images/logo.jpg"},
    ]
    notices = [
        {"title": "Notice 1", "date": "2025-01-01"},
        {"title": "Notice 2", "date": "2025-01-02"},
    ]
    return render(request, 'pages/home.html', {
        "products": products,
        "notices": notices,
    })