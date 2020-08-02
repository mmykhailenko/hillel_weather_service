from rest_framework import viewsets
import requests
from rest_framework import generics
from rest_framework.response import Response
from .api_key import API_KEY
from .models import Weather, Location, Country
from .serializers import WeatherSerializer
import datetime


class WeatherCreateViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, city=None):
        """
        List all code snippets, or create a new snippet.
        """
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, API_KEY)
        resp = requests.get(url)
        data = resp.json()
        try:
            country = Country.objects.get(name=data['sys']['country'])
        except Country.DoesNotExist:
            country = Country.objects.create(name=data['sys']['country'])
        try:
            location = Location.objects.get(city=data['name'], country=Country.objects.get(id=country.id),
                                            longitude=data['coord']['lon'],
                                            latitude=data['coord']['lat'])
        except Location.DoesNotExist:
            location = Location.objects.create(city=data['name'], country=Country.objects.get(id=country.id),
                                               longitude=data['coord']['lon'],
                                               latitude=data['coord']['lat'])
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        weather = Weather.objects.create(
            precipitation=data['weather'][0]['description'], location=Location.objects.get(city=location.city),
            temperature=data['main']['temp'],
            temp_feels_like=data['main']['feels_like'],
            temp_min=data['main']['temp_min'],
            temp_max=data['main']['temp_max'], pressure=data['main']['pressure'],
            humidity=data['main']['humidity'], visibility=data['visibility'],
            wind_speed=data['wind']['speed'], wind_deg=data['wind']['deg'],
            cloud_counter=data['clouds']['all'], datetime=date)
        need_city = Location.objects.get(city=city)
        queryset = Weather.objects.filter(location=need_city.id, datetime=date)
        serializer = WeatherSerializer(queryset, many=True)
        return Response({f"{weather.location}": serializer.data})

    def get_by_coordinates(self, request, lat, lon):
        """
                List all code snippets, or create a new snippet.
        """
        url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(lat, lon,
                                                                                                          API_KEY)
        response = requests.get(url)
        data = response.json()
        try:
            country = Country.objects.get(name=data['sys']['country'])
        except Country.DoesNotExist:
            country = Country.objects.create(name=data['sys']['country'])
        try:
            location = Location.objects.get(city=data['name'], country=Country.objects.get(id=country.id),
                                            longitude=data['coord']['lon'],
                                            latitude=data['coord']['lat'])
        except Location.DoesNotExist:
            location = Location.objects.create(city=data['name'], country=Country.objects.get(id=country.id),
                                               longitude=data['coord']['lon'],
                                               latitude=data['coord']['lat'])
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        weather = Weather.objects.create(
            precipitation=data['weather'][0]['description'], location=Location.objects.get(id=location.id),
            temperature=data['main']['temp'],
            temp_feels_like=data['main']['feels_like'],
            temp_min=data['main']['temp_min'],
            temp_max=data['main']['temp_max'], pressure=data['main']['pressure'],
            humidity=data['main']['humidity'], visibility=data['visibility'],
            wind_speed=data['wind']['speed'], wind_deg=data['wind']['deg'],
            cloud_counter=data['clouds']['all'], datetime=date)
        need_location = Location.objects.get(longitude=lon, latitude=lat)
        queryset = Weather.objects.filter(location=need_location.id, datetime=date)
        serializer = WeatherSerializer(queryset, many=True)
        return Response({f"{weather.location}": serializer.data})


class WeatherViewSet(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
