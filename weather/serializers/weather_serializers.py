from rest_framework import serializers
from weather.models.weather_models import Weather
from weather.serializers.location_serializers import LocationSimpleSerializer


class WeatherSerializer(serializers.ModelSerializer):
    location = LocationSimpleSerializer(many=True)

    class Meta:
        model = Weather
        fields = (
            "id",
            "temperature",
            "temp_feels_like",
            "temp_min",
            "temp_max",
            "pressure",
            "humidity",
            "visibility",
            "wind_deg",
            "wind_speed",
            "location",
            "description",
        )
