from rest_framework import serializers
from .models import person,product

class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'