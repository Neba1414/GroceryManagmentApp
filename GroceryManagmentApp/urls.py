from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LandingPage.urls')),
    path('', include('RegistrationPage.urls')),
]