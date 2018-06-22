
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from pr1.views import *


urlpatterns = [
    path('admin/', admin),
    path('admin_add/', cyber_forum_view),
    path('admin/articles/add/', add),
    path('admin/articles/', article),
    path('', main_page),
    path('', include('pr1.urls')),
    re_path('^element/(?P<j>\w+)/$', rabota),
    re_path('^articles/(?P<j>\w+)/$', rabota),
    path('registration/', login_new_func),
    re_path('^email_conf/(?P<user_login>\w+)/$', check_from_email)
]
