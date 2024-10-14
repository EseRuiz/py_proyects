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
    task = models.CharField(max_length = 250, verbose_name= 'tarea')
    description = models.CharField(max_length = 250, verbose_name= 'descripcion')
    name = models.CharField(max_length = 125, verbose_name= 'nombre')
