from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.name
