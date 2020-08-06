from django.shortcuts import render, redirect
import requests
from rest_framework import generics, viewsets
from rest_framework.response import Response
from weather.api_key import API_KEY, api_url_city, api_url_coord
from weather.forms import NameForm, CoordForm
from weather.models import Weather, Location, Country
from weather.serializers import WeatherSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class WeatherCreateViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    weather_list = list()
    context = {'weathers': weather_list}

    def creating(self, resp):
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

        for weather_data in serializer.data.get('location'):
            res = {
                'city': weather_data['city'],
                'temperature': serializer.data.get('temperature'),
                'flag': weather_data['country']['flag'],
            }
            self.weather_list.append(res)

    def create(self, request, *args, **kwargs):
        form_city = NameForm(request.POST)
        form_coord = CoordForm(request.POST)
        if form_city.is_valid():
            city = form_city.cleaned_data['city']
            url = api_url_city.format(city, API_KEY)
            if url is not None:
                resp = requests.get(url).json()
            else:
                Response("ERROR")
            self.creating(resp)
        elif form_coord.is_valid():
            lat = form_coord.cleaned_data['lat']
            lon = form_coord.cleaned_data['lon']
            url = api_url_coord.format(lat, lon, API_KEY)
            if url is not None:
                resp = requests.get(url).json()
            else:
                Response("ERROR")
            self.creating(resp)

        return redirect('/weather')

    def list(self, request, *args, **kwargs):
        queryset = Weather.objects.all()
        serializer = WeatherSerializer(queryset, many=True)
        return render(request, 'weather/index.html', self.context)


