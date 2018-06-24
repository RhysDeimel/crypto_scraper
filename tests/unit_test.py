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

    def test_filter_only_coins_returns_list_of_coindicts(self, data_loader):
        raw_response = data_loader('miningpoolhub_small.json')
        snapshot = coinpool.MiningPoolHub()
        only_coins = snapshot.filter_only_coins(raw_response)
        assert len(only_coins) == 3

    def test_confirmed_coins_returns_only_confirmed_value(self, data_loader):
        given = data_loader('coin_list.json')
        expected = data_loader('confirmed_coin_list.json')
        snapshot = coinpool.MiningPoolHub()
        confirmed = snapshot.confirmed_coins(given)

        assert confirmed == expected

@pytest.fixture
def data_loader():

    def open_file(filename):
        with open("tests/data/{}".format(filename), 'r') as f:
            return json.load(f)

    return open_file

# @pytest.fixture
# def coin_list():
#     with open("tests/data/coin_list.json", 'r') as f:
#         return json.load(f)
#
# @pytest.fixture
# def confirmed_coin_list():
#     with open("tests/data/confirmed_coin_list.json", 'r') as f:
#         return json.load(f)
