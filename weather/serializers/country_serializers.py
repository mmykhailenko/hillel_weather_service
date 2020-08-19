from rest_framework import serializers
from weather.models.country_models import Country


class CountrySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            "name",
            "flag",
            "wiki_page",
        )
