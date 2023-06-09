from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, cars_sorted, cars_sorted_by_model

# Crea el enrutador
router = DefaultRouter()
router.register(r"cars", CarViewSet)

# Agrega las rutas para las vistas de clasificación
urlpatterns = [
    *router.urls,
    path("cars/sorted/<str:order>/", cars_sorted, name="cars_sorted"),
    path(
        "cars/sorted/model/<str:order>/",
        cars_sorted_by_model,
        name="cars_sorted_by_model",
    ),
]
