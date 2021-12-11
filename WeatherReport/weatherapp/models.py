from django.db import models

# Create your models here.

class WeatherReport(models.Model):
    city_name = models.CharField(max_length=100, blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    temperature = models.FloatField(blank=False)
    date_of_entry = models.DateField()
