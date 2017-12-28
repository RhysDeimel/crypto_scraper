# Short scraper to pull what crypto I have on miningpoolhub and get prices from
# coinmarketcap.com

# TODO
#   - store instance of object for later use
#   - get crypto since last run (confirmed values only)
#   - get crypto value since last run


import requests
import json
import time
import pprint
import secrets


class Crypto_Assets():
    """Stores a tally of all obtained crypto and value"""

    def __init__(self, testing=False):
        self.time = time.time()
        self.coins = {
            item['coin']: item['confirmed'] for item in
            self._get_raw_miningpoolhub_data(testing)['getuserallbalances']['data']
        }
        self.price = {
            item['id']: float(item['price_aud']) for item in
            self._get_raw_coinmarketcap_data(testing)
            if item['id'] in self.coins.keys()
        }

    def _get_raw_miningpoolhub_data(self, testing):
        """Stub that reads in static file. Replace with API call"""
        if testing:
            stub = open('tests/miningpoolhub_stub.json')
            return json.load(stub)
        else:
            url = 'https://miningpoolhub.com/index.php?page=api&action=getuserallbalances&api_key={}'.format(secrets.api_key)
            r = requests.get(url)
            r.raise_for_status()
            return json.loads(r.text)

    def _get_raw_coinmarketcap_data(self, testing):
        """Stub that reads in static file. Replace with API call"""
        if testing:
            stub = open('tests/coinmarketcap_stub.json')
            return json.load(stub)
        else:
            r = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=AUD&limit=0')
            r.raise_for_status()
            return json.loads(r.text)

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


if __name__ == "__main__":
    assets = Crypto_Assets()
    coin_values = assets.get_value(assets.coins, assets.price)
    total_value = assets.tally_crypto(coin_values)

    print("\nCoins held:")
    pprint.pprint(assets.coins,)
    print("\nValue of individual coins:")
    pprint.pprint(coin_values)
    print("\nTotal: {}\n".format(total_value))
