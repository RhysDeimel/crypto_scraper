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

    def fetch_raw_data(self, url=URL):
        """Calls the api and returns a json blob of coins + amounts"""
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def confirmed_coins(self):
        pass








# Class pool
#     - pool name
#     - date
#     - coin(s) - list of coin objects