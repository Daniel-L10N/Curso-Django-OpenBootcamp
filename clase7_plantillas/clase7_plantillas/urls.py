from django.contrib import admin
from django.urls import path
from .views import simple, dinamico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', simple, name= 'simple'),
    path('dinamico/<str:name>/', dinamico, name= 'dinamico')
]
