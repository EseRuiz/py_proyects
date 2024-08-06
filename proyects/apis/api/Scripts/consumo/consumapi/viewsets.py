from rest_framework import viewsets
from .models import person,product
from .serializer import personSerializer,productSerializer

class personViewSet(viewsets.ModelViewSet):
    queryset = person.objects.all()
    serializer_class = personSerializer

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer