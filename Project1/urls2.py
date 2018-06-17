"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
# from django.contrib.auth import views
from reg_log import views
from django.http import HttpResponse
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

def call_frst_func(request):
    return HttpResponse("Easiest page in my life, I am the best!")


def main_page(request):
    return HttpResponse("Main page, nothing here")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_first_page/', call_frst_func),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('account/logout/', logout, name="logout"),
    # path('account/reset-password/', password_reset, name='reset_password'),
    # path('account/reset-password/done/', password_reset_done, name='reset_password_done'),
    # path('account/reset-password/confirm/', password_reset_confirm, name='password_reset_confirm'),
    # path('account/reset-password/complete/', password_reset_complete, name='password_reset_complete'),

    # path('login/', auth.views.LoginView, name = "login"),
    path('register/', views.RegisterFormView.as_view())
]
