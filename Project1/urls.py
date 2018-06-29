
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from pr1.views import *


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admins),
    path('login/', login),
    path('admins/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('admin_add/', cyber_forum_view),
    path('admin/articles/add/', add),
    path('admin/articles/', article),
    path('', main_page),
    path('', include('pr1.urls')),
    re_path('^element/(?P<j>\w+)/$', rabota),
    re_path('^articles/(?P<j>\w+)/$', rabota),
    re_path('^admin/articles_del/(?P<context>\w+)/$', articles_delete),
    re_path('^admin/articles/edit/(?P<slug>\w+)/$', articles_edit),
    path('registration/', login_new_func),
    re_path('^email_conf/(?P<user_login>\w+)/$', check_from_email)
]
