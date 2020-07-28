from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'api', views.WeatherViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.WeatherViewSet.as_view()),
    path('<slug:city>/', views.WeatherCreateViewSet.as_view({'get': 'retrieve'})),
    path('weah/', include('rest_framework.urls', namespace='rest_framework')),
]
