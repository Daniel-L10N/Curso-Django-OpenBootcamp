from django.contrib import admin
from django.urls import path
from .views import simple

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', simple, name= 'simple')
]
