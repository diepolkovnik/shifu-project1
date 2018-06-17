from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request, 'reg_log/templates/admin_add.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_add/', index),
]