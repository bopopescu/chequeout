from django.urls import path
from . import views

urlpatterns = [
    path('confirmation/', views.confirmation, name="confirmation"),
    path('processing/', views.processing, name="processing"),
    path('success/', views.success, name="success"),
]
