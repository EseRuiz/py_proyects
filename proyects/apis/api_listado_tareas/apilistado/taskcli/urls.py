from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/status/<str:status_code>/', TaskViewSet.as_view({'get': 'list_by_status'}), name='task-list-by-status'),
    path('tasks/<uuid:pk>/update-status/<str:new_status>/', TaskViewSet.as_view({'patch': 'update_status'}), name='task-update-status'),
]

# http://127.0.0.1:8000/api/tasks/  obtener todas las tareas
# http://127.0.0.1:8000/api/task/uuid obtener tarea por uuid
# http://127.0.0.1:8000/api/tasks/status/T/ optener por status
# http://127.0.0.1:8000/api/tasks/<uuid:pk>/update-status/I/  actualizar status por uuid
# http://127.0.0.1:8000/api/tasks/<uuid:pk>/ borrar tarea