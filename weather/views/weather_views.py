import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from weather.forms import CoordForm
from weather.forms import NameForm

from weather.models.country_models import Country
from weather.models.location_models import Location
from weather.models.weather_models import Weather

from weather.serializers.weather_serializers import WeatherSerializer

from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

from utils.get_wiki_page import WikiPageRetrieve
from utils.get_country_flag import CountryFlagRetrieve
from utils.construct_url import UrlConstructor

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]


def serialize_response(resp):
    country_name = resp["sys"]["country"]
    country, _ = Country.objects.get_or_create(
        name=country_name,
        defaults={
            'flag': CountryFlagRetrieve.get_country_flag(country_name),
            'wiki_page': WikiPageRetrieve.get_wiki_page_by_country_code(country_name)}
    )

    location, _ = Location.objects.get_or_create(
        longitude=resp['coord']['lon'],
        latitude=resp['coord']['lat'],
        defaults={'city': resp['name'], 'country': country}
    )

    weather = Weather.objects.create(
        temperature=resp['main']['temp'],
        temp_feels_like=resp['main']['feels_like'],
        temp_min=resp['main']['temp_min'],
        temp_max=resp['main']['temp_max'],
        pressure=resp['main']['pressure'],
        humidity=resp['main']['humidity'],
        visibility=resp['visibility'],
        wind_speed=resp['wind']['speed'],
        wind_deg=resp['wind']['deg'],
        description=resp['weather'][0]['description'],
    )

    weather.location.add(location)
    queryset = Weather.objects.get(id=weather.id)
    serializer = WeatherSerializer(queryset)
    return serializer


class WeatherRetrieveViewSet(generics.RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get(self, request, location):

        try:
            url = UrlConstructor.by_location(location)
        except Exception as exc:
            return exc.__doc__
        if url is not None:
            resp = requests.get(url).json()
        else:
            return JsonResponse("Error")

        serializer = serialize_response(resp)
        context = {'weathers': serializer.data}
        return JsonResponse(context)


class WeatherCreateViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    weather_list = list()
    context = {"weathers": weather_list}

    def creating(self, resp):

        serializer = serialize_response(resp)

        for weather_data in serializer.data.get("location"):
            res = {
                "city": weather_data["city"],
                "temperature": serializer.data.get("temperature"),
                "flag": weather_data["country"]["flag"],
                "wiki_page": weather_data["country"]["wiki_page"],
                "description": serializer.data.get("description"),
            }
            self.weather_list.append(res)

    def create(self, request, *args, **kwargs):
        form_city = NameForm(request.POST)
        form_coord = CoordForm(request.POST)
        url = None
        if form_city.is_valid():
            city = form_city.cleaned_data["city"]
            url = UrlConstructor.by_city(city)

        elif form_coord.is_valid():
            lat = form_coord.cleaned_data["lat"]
            lon = form_coord.cleaned_data["lon"]
            url = UrlConstructor.by_coordinates(lat, lon)

        if url is not None:
            resp = requests.get(url).json()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.creating(resp)

        return redirect("/weather")

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        return render(request, "weather/index.html", {"weathers": self.weather_list})
