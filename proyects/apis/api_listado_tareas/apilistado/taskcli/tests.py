from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task
import uuid

class TaskAPITestCase(APITestCase):
    
    def setUp(self):
        # Crear una tarea de ejemplo
        self.task = Task.objects.create(
            task="Tarea de ejemplo",
            status="T"
        )
        self.task_uuid = self.task.id
        self.list_url = reverse('task-list')
        self.detail_url = reverse('task-detail', kwargs={'pk': self.task_uuid})
        self.status_url = reverse('task-list-by-status', kwargs={'status_code': 'T'})
        self.update_status_url = reverse('task-update-status', kwargs={'pk': self.task_uuid, 'new_status': 'I'})

    def test_get_tasks(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['task'], 'Tarea de ejemplo')
        self.assertEqual(response.data[0]['status_display'], 'TODO')

    def test_get_task_by_uuid(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.task_uuid))
        self.assertEqual(response.data['task'], 'Tarea de ejemplo')
        self.assertEqual(response.data['status_display'], 'TODO')

    def test_post_create_task(self):
        data = {
            "task": "Nueva tarea",
            "status": "T"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['task'], "Nueva tarea")
        self.assertEqual(response.data['status_display'], "TODO")

    def test_patch_update_task_status(self):
        response = self.client.patch(self.update_status_url, {'status': 'I'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'I')
        self.assertEqual(response.data['status_display'], 'IN-PROGRESS')

    def test_put_update_task(self):
        data = {
            "task": "Tarea actualizada",
            "status": "D"
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['task'], "Tarea actualizada")
        self.assertEqual(response.data['status'], 'D')
        self.assertEqual(response.data['status_display'], 'DONE')

    def test_get_tasks_by_status(self):
        response = self.client.get(self.status_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['task'], 'Tarea de ejemplo')
        self.assertEqual(response.data[0]['status_display'], 'TODO')
