from .views import estaticos
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estaticos/', estaticos, name='static')
]
