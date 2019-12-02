from django.contrib import admin

from django.urls import path

from .views import BlogPostRudView,BlogPostCreateView

urlpatterns = [
    path('',BlogPostCreateView.as_view(), name = "post-create" ),
    path('<int:pk>/',BlogPostRudView.as_view(), name = "post-rud" ),
]
