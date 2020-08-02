import requests
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from weather.models import Country
from weather.models import Location
from weather.models import Weather
from weather.serializers import WeatherSerializer


class WeatherListViewSet(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class WeatherRetrieveViewSet(generics.RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get(self, request, *args, **kwargs):
        API_KEY = "4fa4301a4a602a89d861783928c0a919"
        location = kwargs.get('location')
        url = None
        if location.startswith('lon') or location.startswith('lat'):
            url = 'http://api.openweathermap.org/data/2.5/weather?{}&appid={}'.format(location, API_KEY)
        elif location.startswith('q'):
            url = "http://api.openweathermap.org/data/2.5/weather?{}&appid={}".format(location, API_KEY)

        if url is not None:
            resp = requests.get(url).json()
        else:
            Response("ERROR")
        country_name = resp['sys']['country']
        country, _ = Country.objects.get_or_create(
            name=country_name,
            defaults={
                'flag': 'https://www.countryflags.io/{}/shiny/64.png'.format(country_name),
                'wiki_page': 'TBD'
            }
        )
        location, _ = Location.objects.get_or_create(
            longitude=resp['coord']['lon'],
            latitude=resp['coord']['lat'],
            defaults={'city': resp['name'], 'country': country}
        )
        weather = self.queryset.create(
            temperature=resp['main']['temp'],
            temp_feels_like=resp['main']['feels_like'],
            temp_min=resp['main']['temp_min'],
            temp_max=resp['main']['temp_max'],
            pressure=resp['main']['pressure'],
            humidity=resp['main']['humidity'],
            visibility=resp['visibility'],
            wind_speed=resp['wind']['speed'],
            wind_deg=resp['wind']['deg']
        )
        weather.location.add(location)
        queryset = Weather.objects.get(id=weather.id)
        serializer = WeatherSerializer(queryset)

        weather_list = list()
        for weather_data in serializer.data.get('location'):
            res = {
                'city': weather_data['city'],
                'temperature': serializer.data.get('temperature'),
                'flag': weather_data['country']['flag'],
            }
            weather_list.append(res)

        context = {'weathers': weather_list}
        return render(request, 'index.html', context)
