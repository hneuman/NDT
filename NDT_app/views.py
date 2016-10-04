from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'main.html',)


def inicio(request):
    return render(request, 'principal.html',)

def quienes_somos(request):
    return render(request, 'somos.html',)

def contacto(request):
    return render(request, 'contacto.html',)

def productos(request):
    return render(request, 'productos.html',)
