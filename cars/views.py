from django.shortcuts import render

# Create your views here.


# En el archivo views.py de tu aplicación

from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
