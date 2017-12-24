# Short scraper to pull what crypto I have on miningpoolhub and get prices from
# coinmarketcap.com

# Would like to:
#   - get all cryto I have
#     - leave it open to check wallets or other pools in the future
#   - get absolute value of all crypto (confirmed values only)
#   - get crypto since last run (confirmed values only)
#   - get crypto value since last run
#   - display in AUD


# call to coinmarketcap:
# https://api.coinmarketcap.com/v1/ticker/?convert=AUD
#
# is probs quicker to get all values, and isolate the ones needed, rather than
# make serparate API calls for each coin

import requests
import json

#############
# API calls
#############

# TODO: Change mocks below to actual calls that work with testing
#   - make a secrets file to store API keys


#############
# Processing
#############

class Crypto_Assets():
    """Stores a tally of all obtained crypto and value"""

    def __init__(self):
        self.coins = {
            item['coin']: item['confirmed'] for item in
            self.get_raw_miningpoolhub_data()['getuserallbalances']['data']
        }
        self.price = {
            item['id']: float(item['price_aud']) for item in
            self.get_raw_coinmarketcap_data()
            if item['id'] in self.coins.keys()
        }

    def get_raw_miningpoolhub_data(self):
        """Stub that reads in static file. Replace with API call"""
        stub = open('tests/miningpoolhub_stub.json')
        return json.load(stub)

    def get_raw_coinmarketcap_data(self):
        """Stub that reads in static file. Replace with API call"""
        stub = open('tests/coinmarketcap_stub.json')
        return json.load(stub)

    def get_value(self, coin_dict, price_dict):
        """Given a dictionary of coins, will return the AUD value of held coins"""
        coins = coin_dict.copy()

        for k, v in coin_dict.items():
            coin_price = price_dict.get(k, None)
            if not coin_price:
                coins[k] = 'No price data'
                continue
            coins[k] = round(v * coin_price, 2)

        return coins

    def tally_crypto(self, coin_value_dict):
        """Returns the total price in AUD of all coins held"""

        # Making sure that we catch the super unlikely chance an int gets passed
        assert not [v for v in coin_value_dict.values() if type(v) == int]

        coin_values = [v for v in coin_value_dict.values() if type(v) == float]
        return sum(coin_values)


# TODO: store instance of object for later use
#   - comparing how much crypto earnt since last run
#   - comparing value of earnt crypto since last run
#   - add timestamp for future data analysis?
