from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {'nombre':'Daniel'})

def dinamico(request, name):
    print(type(name))
    categorias = ['basos', 'copas', 'tamques']
    print(name)
    return render(request, 'dinamico.html', {'name':name, 'categorys': categorias})