from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['id', 'task', 'status', 'status_display', 'created_at', 'updated_at']

    def get_status_display(self, obj):
        return obj.get_status_display()