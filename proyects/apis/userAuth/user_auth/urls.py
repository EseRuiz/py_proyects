from django.urls import path
from .viewsets import RegisterView, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]