from django.contrib import admin
from weather.models.country_models import Country
from weather.models.weather_models import Weather
from weather.models.location_models import Location

# Register your models here.
admin.site.register(Weather)
admin.site.register(Location)
admin.site.register(Country)
