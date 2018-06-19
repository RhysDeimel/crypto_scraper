import time
from crypto_scraper import coinpool


class TestPool:
    pass


class TestMiningPoolHub:

    def test_two_instances_have_different_date_values(self):
        first = coinpool.MiningPoolHub()
        time.sleep(1)
        second = coinpool.MiningPoolHub()

        assert first.date != second.date


