from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.product_list, name="product_list"),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('comment/create/<int:product_id>/', views.comment_create, name='comment_create'),
    path('comment/<int:comment_id>/update/', views.comment_update, name='comment_update'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]