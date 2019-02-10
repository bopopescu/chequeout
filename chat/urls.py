from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.chat, name="chat"),
    path('message/dialog/', views.dialog, name="dialog"),
    path('message/result/', views.result, name="result")
]
