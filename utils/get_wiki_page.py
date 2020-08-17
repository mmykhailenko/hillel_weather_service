import wikipedia
import pycountry
import logging


class WikiPageRetrieve(object):

    @staticmethod
    def get_country_by_code(country_code):
        if len(country_code) == 2:
            try:
                return pycountry.countries.get(alpha_2=country_code).name
            except Exception:
                logging.exception('')
                return "CountryNotFoundError"
        elif len(country_code) == 3:
            try:
                return pycountry.countries.get(alpha_3=country_code).name
            except Exception:
                logging.exception('')
                return "CountryNotFoundError"
        else:
            return 'Error code'

    @staticmethod
    def get_wiki_page_by_country_name(country_name):
        wikipedia.set_lang("en")
        try:
            wikipage = wikipedia.page(country_name)
            return wikipage.url
        except wikipedia.exceptions as e:
            logging.exception('')

    @staticmethod
    def get_wiki_page_by_country_code(country_code):
        wiki_page = \
            WikiPageRetrieve.get_wiki_page_by_country_name(WikiPageRetrieve.get_country_by_code(country_code))
        return wiki_page
