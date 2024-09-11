from django.db import models
import uuid

class Task(models.Model):
    """ 
    Simple tracking of tasks
    
    """
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    STATUS = [
        ('T', 'TODO'),
        ('I', 'IN-PROGRESS'),
        ('D', 'DONE'),
    ]
    task = models.CharField(max_length= 250, verbose_name= 'tarea')
    status = models.CharField(max_length= 1, choices= STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_status_display(self):
        return dict(self.STATUS).get(self.status)