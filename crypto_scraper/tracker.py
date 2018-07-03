import datetime


class Tracker:

    def __init__(self):
        self.date = datetime.datetime.now()


class CoinMarketCap(Tracker):

    # URL = "https://api.coinmarketcap.com/v1/ticker/?convert=AUD&limit=0"

    def __init__(self):
        super().__init__()
        self.name = "CoinMarketCap"

    def fetch_raw_data(self):
        """Paginate through all coins and return json"""
        payload = {'start': 0, 'sort': 'id'}
        r = requests.get("https://api.coinmarketcap.com/v2/ticker/", params=payload)

        