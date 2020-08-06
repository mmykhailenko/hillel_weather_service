import wikipedia
import pycountry


def get_country_from_code(country_code):
    if len(country_code) == 2:
        return pycountry.countries.get(alpha_2=country_code).name
    elif len(country_code) == 3:
        return pycountry.countries.get(alpha_3=country_code).name
    else:
        return 'Error code'


def get_wiki_page(country_code):
    wikipedia.set_lang("en")
    wikipage = wikipedia.page(get_country_from_code(country_code))
    return wikipage.url


print(get_wiki_page('UA'))