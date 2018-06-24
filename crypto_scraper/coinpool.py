import requests
import datetime
import secrets


class Pool:

    def __init__(self):
        self.date = datetime.datetime.now()


class MiningPoolHub(Pool):
    URL = ("https://miningpoolhub.com/index.php?"
           "page=api&action=getuserallbalances"
           "&api_key={}".format(secrets.api_key))

    def __init__(self, coins=None):
        super().__init__()
        self.name = "MiningPoolHub"
        if not coins:
            self.coins = self.filter_only_coins()

    def fetch_raw_data(self, url=URL):
        """Calls the api and returns a raw api json response cointaining coins +
         amounts"""
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def filter_only_coins(self, raw_json=None):
        """Return a list of dicts containing coin information"""
        if not raw_json:
            raw_json = self.fetch_raw_data()
        return raw_json['getuserallbalances']['data']

    def confirmed_coins(self, coin_list=None):
        """Return list of dicts containing coin name and confirmed value"""
        if not coin_list:
            coin_list = self.coins
        return [{'coin': d['coin'], 'confirmed': d['confirmed']}
                     for d in coin_list]






# Class pool
#     - pool name
#     - date
#     - coin(s) - list of coins