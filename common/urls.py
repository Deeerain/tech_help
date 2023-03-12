from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('works/', views.WorkView.as_view(), name='works'),
    path('works/<int:pk>/', views.remove_work, name='works_delete'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('auth/', LoginView.as_view(), name='auth'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/logout-then-login/', logout_then_login, name='logout-then-login'),
]
