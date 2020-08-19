from rest_framework import serializers
from weather.models.location_models import Location
from weather.serializers.country_serializers import CountrySimpleSerializer


class LocationSimpleSerializer(serializers.ModelSerializer):
    country = CountrySimpleSerializer()

    class Meta:
        model = Location
        fields = (
            "city",
            "country",
            "longitude",
            "latitude",
        )
