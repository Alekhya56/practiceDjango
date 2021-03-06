from django.contrib import admin

from django.urls import path

from django.contrib.auth import views as auth_views

from .views import register_view, profile


urlpatterns =[
    path('register/', register_view, name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = "login.html"), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
]