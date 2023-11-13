from django.shortcuts import render

def home(request):
    return render(request, 'GimApp/home.html')

def agregar_clientes(request):
    return render (request, 'GimApp/agregar_clientes.html')