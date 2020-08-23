import os
PUBLIC_WEATHER_API_KEY = os.environ.get("PUBLIC_WEATHER_API_KEY")
PUBLIC_WEATHER_API_PATH = os.environ.get("PUBLIC_WEATHER_API_PATH")
PUBLIC_WEATHER_API_UNITS = os.environ.get("PUBLIC_WEATHER_API_UNITS")


class UrlConstructor(object):

    @staticmethod
    def by_city(city):
        city_url = f"{PUBLIC_WEATHER_API_PATH}?q={city}&{PUBLIC_WEATHER_API_KEY}&{PUBLIC_WEATHER_API_UNITS}"
        return city_url

    @staticmethod
    def by_coordinates(lat, lon):
        coord_url = f"{PUBLIC_WEATHER_API_PATH}?lat={lat}&lon={lon}&{PUBLIC_WEATHER_API_KEY}&{PUBLIC_WEATHER_API_UNITS}"
        return coord_url

    @staticmethod
    def by_location(location):
        if location.startswith('lon') or location.startswith('lat'):
            location_url = f"{PUBLIC_WEATHER_API_PATH}?{location}&{PUBLIC_WEATHER_API_KEY}&{PUBLIC_WEATHER_API_UNITS}"
            return location_url
        elif location.startswith('q'):
            location_url = f"{PUBLIC_WEATHER_API_PATH}?{location}&{PUBLIC_WEATHER_API_KEY}&{PUBLIC_WEATHER_API_UNITS}"
            return location_url
        else:
            return "Location Not Found"
