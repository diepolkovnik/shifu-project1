
from django.contrib import admin
from django.urls import path, re_path
from pr1.views import cyber_forum_view, main_page, rabota


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_add/', cyber_forum_view),
    path('', main_page),
    re_path('^element/(?P<j>\w+)/$', rabota),
]
