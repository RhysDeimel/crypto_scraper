from crypto_scraper import coinpool
from crypto_scraper import tracker


class TestMiningPoolHub:
    pass

    # def test_fetch_raw_data_returns_json_coin_blob(self):
    #     # will have to roll my own webserver to test this. Flask?
    #     assert False


class TestCoinMarketCap:
    pass

    # test fetch_raw_data paginates
    # make sure sort == id and 'start' is incrementing by 100
    # return below after a few iterations
    # {
    # "data": null, 
    #     "metadata": {
    #         "timestamp": 1530612543, 
    #         "error": "id not found"
    #     }
    # }

    # test fetch_raw_data returns combined json blob