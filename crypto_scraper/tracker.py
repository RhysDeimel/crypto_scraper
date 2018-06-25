import datetime


class Tracker:

    def __init__(self):
        self.date = datetime.datetime.now()


class CoinMarketCap(Tracker):

    URL = "https://api.coinmarketcap.com/v1/ticker/?convert=AUD&limit=0"

    def fetch_raw_data(self):
        pass