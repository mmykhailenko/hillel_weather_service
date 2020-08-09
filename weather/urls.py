from django.urls import include, path
from django.conf.urls import url
from weather import views
from weather.models import Weather
from django.views.generic import ListView

urlpatterns = [
    path("", views.WeatherCreateViewSet.as_view({"get": "list", "post": "create"}), name='weather'),
    path('<str:location>/', views.WeatherRetrieveViewSet.as_view()),
]
