import datetime


class Pool:

    def __init__(self):
        self.date = datetime.datetime.now()


class MiningPoolHub(Pool):
    # URL = ("https://miningpoolhub.com/index.php",
    #        "?page=api&action=getuserallbalances",
    #        "&api_key={}")

    def __init__(self):
        super().__init__()
        self.name = "MiningPoolHub"
        self.base_url = "https://miningpoolhub.com/index.php"

    def fetch_raw_data():
        """Calls the api and returns a json blob of coins + amounts"""
        pass








# Class pool
#     - pool name
#     - date
#     - coin(s) - list of coin objects