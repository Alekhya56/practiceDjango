from django.contrib import admin
from django.urls import path
from .views import profile, register_view, update_profile

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile_update', update_profile, name = 'profile-update'),
    path('',register_view,name = "register"),
]