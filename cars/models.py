from django.db import models
from django.core.exceptions import ValidationError


def validate_price(price):
    if price < 0:
        raise ValidationError("Invalid price!")


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    model = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Description(models.Model):
    car = models.ForeignKey(
        Car, related_name="descriptions", on_delete=models.CASCADE, default=None
    )
    text = models.TextField()

    def __str__(self):
        return self.text
