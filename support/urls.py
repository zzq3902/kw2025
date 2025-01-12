from django.urls import path
from . import views


urlpatterns = [
    path("notice/", views.notice, name="notice"),
    path("inquiry/", views.inquiry, name="inquiry"),
]