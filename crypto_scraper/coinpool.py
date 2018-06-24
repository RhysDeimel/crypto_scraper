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

    def __init__(self):
        super().__init__()
        self.name = "MiningPoolHub"
        self.raw_data = ''
        self.coins = ''

    def fetch_raw_data(self, url=URL):
        """Calls the api and returns a raw api json response cointaining coins +
         amounts"""
        if not url:
            pass
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def filter_only_coins(self, raw_api_json):
        """Return a list of dicts containing coin information"""
        return raw_api_json['getuserallbalances']['data']

    def confirmed_coins(self, coin_list):
        """Return list of dicts containing coin name and confirmed value"""
        return [{'coin': d['coin'], 'confirmed': d['confirmed']}
                     for d in coin_list]








# Class pool
#     - pool name
#     - date
#     - coin(s) - list of coins