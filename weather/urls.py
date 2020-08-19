from django.urls import include, path
from django.conf.urls import url
from weather.views.weather_views import WeatherCreateViewSet
from weather.views.weather_views import WeatherRetrieveViewSet
from weather.models.weather_models import Weather
from django.views.generic import ListView

urlpatterns = [
    path("", WeatherCreateViewSet.as_view({"get": "list", "post": "create"}), name='weather'),
    path('<str:location>/', WeatherRetrieveViewSet.as_view()),
]
