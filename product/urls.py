from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.product_list, name="product_list"),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]