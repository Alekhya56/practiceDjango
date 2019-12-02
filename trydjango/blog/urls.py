from django.contrib import admin

from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [ 
    path('create/', ArticalCreateView.as_view(), name ='create'),
    path('list', ArticalListView.as_view(), name ='list'),
    path('<int:id>/detail/', ArticalDetailView.as_view(), name ='detail'),
    path('<int:id>/delete/', ArticalDeleteView.as_view(), name ='delete'),
    path('<int:id>/update', ArticalUpdateView.as_view(), name ='update')
]