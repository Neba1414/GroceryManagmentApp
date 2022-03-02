from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registrationPage, name="register"),
]