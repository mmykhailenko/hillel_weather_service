from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=3)


class Location(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.city}, {self.country.name}"


class Weather(models.Model):
    precipitation = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
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
    datetime = models.DateTimeField(blank=True, null=True)
