from django.contrib import admin

from django.urls import path

from .views import *

app_name = 'Products'

urlpatterns=[
    path('create/', product_create_view, name ='create'),
    path('delete/<int:my_id>/',product_delete_view , name= 'delete' ),
    path('list/', product_list_view, name = 'list'),
    path('detail/<int:my_id>/', product_detail_view, name ='detail'),
    path('initial/', render_initial_data, name ='initial'),
    path('dynamic/<int:my_id>/', dynamic_lookup_view, name= 'dynamic' ),
]