
from django.urls import path

from weather import views

urlpatterns = [
    path('', views.WeatherListViewSet.as_view()),
    path('<str:location>/', views.WeatherRetrieveViewSet.as_view()),
]
