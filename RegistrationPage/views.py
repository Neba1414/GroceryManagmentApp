from django.shortcuts import render

def registrationPage(request):
    return render(request, "RegistrationPage/RegistrationForm.html")