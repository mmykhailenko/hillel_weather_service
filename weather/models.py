from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    flag = models.CharField(max_length=512, null=True, blank=True)
    wiki_page = models.CharField(max_length=512, null=True, blank=True)


class Location(models.Model):
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('longitude', 'latitude')


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
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
