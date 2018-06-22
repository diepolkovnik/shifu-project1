
from django.contrib import admin
from django.urls import path, re_path
from pr1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_add/', cyber_forum_view),
    path('', main_page),
    path('', include('pr1.urls')),
    re_path('^element/(?P<j>\w+)/$', rabota),
    path('registration/', login_new_func),
    re_path('^email_conf/(?P<user_login>\w+)/$', check_from_email)
]
