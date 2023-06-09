from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


@api_view(["GET"])
def cars_sorted(request, order):
    if order == "asc":
        cars = Car.objects.order_by("price")
    elif order == "desc":
        cars = Car.objects.order_by("-price")
    else:
        return Response({"error": "Invalid order parameter"}, status=400)

    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def cars_sorted_by_model(request, order):
    if order == "asc":
        cars = Car.objects.order_by("model")
    elif order == "desc":
        cars = Car.objects.order_by("-model")
    else:
        return Response({"error": "Invalid order parameter"}, status=400)

    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
