
from django.contrib import admin
from django.urls import path
from .views import bienvenido, despedida, sumar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='inicio'),
    path('despedida/', despedida, name='exit'),
    path('sumar/<int:num1>/<int:num2>/', sumar, name='suma')
]
