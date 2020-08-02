import json

import requests
from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request, city=None):
    API_KEY = "4fa4301a4a602a89d861783928c0a919"
    CITY_NAME = city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API_KEY}'.format(CITY=CITY_NAME,                                                                                                   API_KEY=API_KEY)
    city_weather = requests.get(url).json() #request the API data and convert the JSON to Python data types
    return render(request, 'weather/index.html') #returns the index.html template