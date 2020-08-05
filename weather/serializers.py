from rest_framework import serializers

from .models import Weather, Location, Country


class CountrySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            'name',
            'flag',
            'wiki_page',
        )


class LocationSimpleSerializer(serializers.ModelSerializer):
    country = CountrySimpleSerializer()

    class Meta:
        model = Location
        fields = (
            'city',
            'country',
            'longitude',
            'latitude',
        )


class WeatherSerializer(serializers.ModelSerializer):
    location = LocationSimpleSerializer(many=True)

    class Meta:
        model = Weather
        fields = (
            'id',
            'temperature',
            'temp_feels_like',
            'temp_min',
            'temp_max',
            'pressure',
            'humidity',
            'visibility',
            'wind_deg',
            'wind_speed',
            'location',
        )

