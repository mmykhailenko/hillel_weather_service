from django.db import models
from weather.models.location_models import Location


class Weather(models.Model):
    location = models.ManyToManyField(Location)
    temperature = models.CharField(max_length=20)
    temp_feels_like = models.CharField(max_length=20)
    temp_min = models.CharField(max_length=20)
    temp_max = models.CharField(max_length=20)
    pressure = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)
    visibility = models.CharField(max_length=20)
    wind_speed = models.CharField(max_length=20)
    wind_deg = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
