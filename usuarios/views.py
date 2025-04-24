from django.shortcuts import render

def home(request):
    return render(request, 'usuarios/home.html')

def landing(request):
    return render(request, 'landing.html')