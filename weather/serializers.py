from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ['country', 'city', 'longitude', 'latitude', 'status', 'temperature', 'temp_feels_like', 'temp_min',
                  'temp_max', 'pressure', 'humidity', 'visibility', 'wind_speed', 'wind_deg', 'cloud_counter']

