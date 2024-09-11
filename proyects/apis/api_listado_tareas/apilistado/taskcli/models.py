from django.db import models

class Task(models.Model):
    STATUS = { "T": "TODO" , "I" : "IN-PROGRESS" , "D" : "DONE"}
    task = models.CharField(max_length= 250, verbose_name= 'tarea')
    status = models.CharField(max_length= 1, choices= STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
