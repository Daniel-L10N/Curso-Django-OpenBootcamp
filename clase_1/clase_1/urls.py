from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo),
    path('despedida/', views.despedida),
    path('adulto/<int:edad>/', views.adulto),
]
