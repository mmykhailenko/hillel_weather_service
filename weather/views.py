import json

import requests
from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        API_KEY = "4fa4301a4a602a89d861783928c0a919"
        CITY_NAME = "Odessa"
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(CITY_NAME, API_KEY)
        resp = requests.get(url)
        return JsonResponse(json.loads(resp.text))
