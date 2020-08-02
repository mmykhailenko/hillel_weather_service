from rest_framework import serializers
from .models import Weather, Location


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['location', 'precipitation', 'temperature', 'temp_feels_like', 'temp_min',
                  'temp_max', 'pressure', 'humidity', 'visibility', 'wind_speed', 'wind_deg', 'cloud_counter',
                  'datetime']

