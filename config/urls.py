from django.contrib import admin
from django.urls import path, include


admin.site.site_title = 'TechHelp'
admin.site.site_header = 'Панель управления TechHelp'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', include('common.urls')),
]
