import requests
from requests.auth import HTTPBasicAuth
import re
from itertools import islice


def get_auctions(region, server, amount):
    # requesting an oauth token to be able to access blizzards api's / client id and secret id required
    response = requests.post("https://eu.battle.net/oauth/token", data={"grant_type": 'client_credentials'},
                             auth=HTTPBasicAuth('d6df743cb1b94e9c9fe1521e844514f8',
                                                'yDTfM7hSYIzpXR55O4KDkJ1PHweo5inx')).json()

    # the call to blizzards api, server is decided by the user
    api_url = f"https://{region}.api.blizzard.com/wow/auction/data/{server}?locale=en_eu&access_token="

    # the access token is needed to make the call, it gets added in the back of the string
    # this call returns a json object with an url that displays all the data in a json format
    auction_data = requests.get(api_url + response.get('access_token')).content

    # extracts the url from the json object above and saves it in a list
    url = re.findall('(?<=\:\").+?(?=\"\,)', format(auction_data))

    # the findall method saves the data in a list of strings - extracting the url and saves it in a string
    url = url[0]

    # fetches all the raw auctions from the url which comes in a json format, removes the things we don't need
    raw_auctions = requests.get(url).json().get('auctions')

    # counts number of current auctions on the selected server, saving it in a static variable
    get_auctions.number_of_auctions = 0
    for auction in raw_auctions:
        get_auctions.number_of_auctions += 1

    # the amount of auctions displayed on a server are enormous (50.000+), displaying a desired number to show it works
    def take(iterable, n):
        # using islice to return n amount of items as a list
        return list(islice(iterable, n))

    n_items = take(raw_auctions, amount)

    return n_items
