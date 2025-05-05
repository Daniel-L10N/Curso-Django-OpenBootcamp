from django.shortcuts import render

def estaticos(request):
    return render(request, 'static.html', {})