from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    flag = models.CharField(max_length=512)
    wiki_page = models.CharField(max_length=512)


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()

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
    pub_date = models.DateTimeField(auto_now_add=True)
