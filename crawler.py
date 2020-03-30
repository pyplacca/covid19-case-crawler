import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

URL = 'https://www.worldometers.info/coronavirus/'
AGENT = {'User-Agent': 'Chrome'}
html = url_data = None


A = COUNTRY = 'Country, Other'
B = CASES = 'Total Cases'
C = NEW_CASES = 'New Cases'
D = DEATHS = 'Total Deaths'
E = NEW_DEATHS = 'New Deaths'
F = RECOVERED = 'Total Recovered'
G = ACTIVE = 'Active Cases'
H = CRITICAL = 'Serious, Critical'
I = CASES_MIL = 'Total Cases / 1M population'
J = DEATHS_MIL = 'Total deaths / 1M population'
K = CASE_1 = 'First case'

heads = 11
table_heads = dict(zip(
    [A, B, C, D, E, F, G, H, I, J, K],
    range(heads)
))
countries = {}


def searchCountry(name):
    # name is case-sensitive and must be valid as seen on URL's website
    country = countries[name]
    data = {}
    
    for key in table_heads:
        data[key] = country.select_one(
            f'td:nth-child({table_heads[key]+1})'
        ).string
    
    return data

def get_url_response(url):
    return urlopen(Request(url, headers=AGENT))

def refresh_data():
    try:
        # establish connection
        url_data = get_url_response(URL)
        countries.clear()
    except urllib.error.URLError:
        print('Please check your internet connection...')

    if url_data:
        # get html page content
        html = BeautifulSoup(url_data.read(), 'html.parser')
        table = html.body.select_one('#main_table_countries_today')

        # build hash from table data
        for tr in table.select('tbody tr'):
            index = table_heads[COUNTRY]
            countries[tr.select('td')[index].string] = tr


# print(searchCountry('USA')[CASES])
