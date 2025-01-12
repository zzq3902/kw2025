from django.urls import path

from . import views

urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('history/', views.history, name='history'),
    path('location/', views.location, name='location'),
]
