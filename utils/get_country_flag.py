from weather.api_key import COUNTRY_FLAG_HOST


class CountryFlagRetrieve(object):

    @staticmethod
    def get_country_flag(country_code):
        country_flag = f"{COUNTRY_FLAG_HOST}/{country_code}/shiny/64.png"
        return country_flag
