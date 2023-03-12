from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('works/', views.WorkView.as_view(), name='works'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('auth/', LoginView.as_view(), name='auth'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
