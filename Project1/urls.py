
from django.contrib import admin
from django.urls import path
from reg_log.views import cyber_forum_view, main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_add/', cyber_forum_view),
    path('', main_page),
]
