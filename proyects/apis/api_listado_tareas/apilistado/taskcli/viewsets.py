from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task
from .serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Consulta por UUID (detalle de la tarea)
    def retrieve(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    # Consulta por estado
    def list_by_status(self, request, status_code=None):
        tasks = Task.objects.filter(status=status_code)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    # Eliminar tarea por UUID
    def destroy(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response({"message": f"Task {pk} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    # Actualizar estado
    def update_status(self, request, pk=None, new_status=None):
        task = get_object_or_404(Task, id=pk)
        task.status = new_status
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
