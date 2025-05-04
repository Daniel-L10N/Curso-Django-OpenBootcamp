from django.http import HttpResponse


def simple(request):
    return HttpResponse('<h1>Hola, Mundo</h1>')