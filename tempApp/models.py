from django.db import models


class TemperatureReading(models.Model):
    id = models.IntegerField(primary_key=True)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class HumidityReading(models.Model):
    id = models.IntegerField(primary_key=True)
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
