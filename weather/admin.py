from django.contrib import admin
from .models import Weather, Location, Country

admin.site.register(Weather)
admin.site.register(Location)
admin.site.register(Country)
# Register your models here.
