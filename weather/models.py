from django.db import models


class Weather(models.Model):
    country = models.CharField(max_length=3)
    city = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.CharField(max_length=20)
    temperature = models.FloatField()
    temp_feels_like = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    visibility = models.IntegerField()
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    cloud_counter = models.IntegerField()

