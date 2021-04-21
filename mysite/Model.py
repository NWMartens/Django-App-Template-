from django.db import models

class Hourly(models.Model):
  TemperatureF = models.CharField(max_length=50)
  TemperatureC = models.CharField(max_length = 50)