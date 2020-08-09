import wikipedia  # pip install wikipedia
import pycountry  # pip install pycountry


def get_country_name(iso_code):
    """Method for get official country name"""
    try:
        country = pycountry.countries.get(alpha_2=iso_code)
        country_name = country.name
        return country_name
    except Exception:
        return "CountryNotFoundError"


def search_wiki_page(country_name):
    """Method for search wiki-page"""
    try:
        wiki = wikipedia.page(country_name)
        return wiki.url
    except wikipedia.exceptions as e:
        print(e)


def main_wiki_search(code):
    """Main function"""
    return search_wiki_page(get_country_name(code))


print(main_wiki_search('US'))
print(main_wiki_search('UA'))
