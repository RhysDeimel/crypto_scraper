import pytest
import time
import json
from crypto_scraper import coinpool
import os


class TestPool:
    pass


class TestMiningPoolHub:

    def test_two_instances_have_different_date_values(self):
        first = coinpool.MiningPoolHub()
        time.sleep(1)
        second = coinpool.MiningPoolHub()

        assert first.date != second.date

    def test_filter_only_coins_returns_list_of_coindicts(small_response):
        # print(os.getcwd())
        print(type(small_response))
        snapshot = coinpool.MiningPoolHub()
        only_coins = snapshot.filter_only_coins(small_response)
        assert len(only_coins) == 3

@pytest.fixture
def small_response():
    with open("tests/data/miningpoolhub_small.json", 'r') as f:
        asdf = json.load(f)
    return asdf

@pytest.fixture
def large_response():
    with open("data/miningpoolhub_large.json", 'r') as f:
        response = json.load(f)
    return response
