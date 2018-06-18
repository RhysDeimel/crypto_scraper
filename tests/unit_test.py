import time
from crypto_scraper import pool


class TestPool:
    pass


class TestMiningPoolHub:

    def test_two_instances_have_different_date_values(self):
        first = pool.MiningPoolHub()
        time.sleep(1)
        second = pool.MiningPoolHub()

        assert first.date != second.date

    def test_fetch_raw_data_returns_json_coin_blob(self):
        assert False
