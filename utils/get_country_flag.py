class CountryFlagRetrieve(object):

    @staticmethod
    def get_country_flag(country_code):
        country_flag = "https://www.countryflags.io/{}/shiny/64.png".format(country_code)
        return country_flag
