from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.index, name="product_list"),
]