from django.shortcuts import render
from django.http import HttpResponse

def bienvenido(request):
    return HttpResponse("<h1> Hola, Bienvenido al programa</h1><a href='/despedida'>Despedir</a>")

def despedida(request):
    context= {'despedida': 'adios'}
    return render(request, 'despedida.html', context)

def sumar(request, num1, num2):
    return HttpResponse(f'{num1} + {num2} = {num1+num2}')