from django.urls import include, path
from django.conf.urls import url
from . import views
from weather.models import Weather
from django.views.generic import ListView

urlpatterns = [
    path('', views.WeatherCreateViewSet.as_view({'get': 'list'})),
    path('post/', views.WeatherCreateViewSet.as_view({'post': 'create'})),
]
