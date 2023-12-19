from django.db import models
from datetime import datetime

# Create your models here.
class Flight(models.Model):
    flight_no = models.CharField(max_length=10)
    origin = models.CharField(max_length=50)
    departure = models.DateTimeField()
    destination = models.CharField(max_length=50)
    arrival = models.DateTimeField()
    price = models.FloatField()  # TODO: add constraints

