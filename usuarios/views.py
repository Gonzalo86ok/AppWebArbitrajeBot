from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def landing(request):
    return render(request, 'landing.html')

def registro(request):
    return render(request, 'registro.html')