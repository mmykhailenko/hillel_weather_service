
from rest_framework import viewsets
import requests
from rest_framework import generics
from rest_framework.response import Response

from .models import Weather
from .serializers import WeatherSerializer


class WeatherCreateViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, city=None):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            API_KEY = "4fa4301a4a602a89d861783928c0a919"
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, API_KEY)
            resp = requests.get(url)
            data = resp.json()
            weather = Weather.objects.create(country=data['sys']['country'], city=data['name'],
                                             longitude=data['coord']['lon'], latitude=data['coord']['lat'],
                                             status=data['weather'][0]['description'], temperature=data['main']['temp'],
                                             temp_feels_like=data['main']['feels_like'],
                                             temp_min=data['main']['temp_min'],
                                             temp_max=data['main']['temp_max'], pressure=data['main']['pressure'],
                                             humidity=data['main']['humidity'], visibility=data['visibility'],
                                             wind_speed=data['wind']['speed'], wind_deg=data['wind']['deg'],
                                             cloud_counter=data['clouds']['all'])
            queryset = Weather.objects.filter(city=city)
            serializer = WeatherSerializer(queryset, many=True)
            return Response({"weather": serializer.data})


class WeatherViewSet(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

