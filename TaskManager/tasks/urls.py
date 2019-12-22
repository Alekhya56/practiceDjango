from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    UserTaskListView
)
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserTaskListView.as_view(), name='user-tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='tasks-detail'),
    path('task/new/', TaskCreateView.as_view(), name='tasks-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='tasks-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='tasks-delete'),
    path('about/', views.about, name='blog-about'),
]
