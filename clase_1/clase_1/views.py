from django.http import HttpResponse
def saludo(request):
    return HttpResponse('Hola mundo')

def despedida(request):
    return HttpResponse('Hasta luego')

def adulto(request, edad):
    print(type(edad))
    print(edad)
    if edad >=18:
        return HttpResponse('eres mayor de edad')
    else:
        return HttpResponse('eres menor de edads')