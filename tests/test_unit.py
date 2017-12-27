# tests here will use a mocked version of miningpoolhub api and coinmarketcap
# api

import crypto_scraper as cs


def test_dict_of_coins_and_values_is_extracted_from_miningpoolhub():
    expected = {"bitcoin": 0.00107096,
                "vertcoin": 0.50628363,
                "feathercoin": 1.40910082,
                "ethereum-classic": 0.00283998,
                "zcash": 0.00027895,
                "zclassic": 0.02357081,
                "zcoin": 0.15349718,
                "monacoin": 0.83877923,
                "zencash": 0.00088039,
                "bitcoin-gold": 0.00197191}

    assets = cs.Crypto_Assets(testing=True)
    assert assets.coins == expected


def test_prices_extracted_from_coinmarketcap_when_held():
    # omits coins not on the exchange
    expected = {"bitcoin": 22684.7153676,
                "vertcoin": 10.0374294907,
                "ethereum-classic": 39.4525977846,
                "zcash": 607.009606632,
                "zcoin": 69.0804662691,
                "monacoin": 18.5676934014,
                "zencash": 43.3666257024,
                "bitcoin-gold": 387.915625383}

    assets = cs.Crypto_Assets(testing=True)
    assert assets.price == expected


def test_get_value_returns_single_correct_price():
    given = {"bitcoin": 0.00107096}
    expected = {"bitcoin": 24.29}
    assets = cs.Crypto_Assets(testing=True)

    assert assets.get_value(given, assets.price) == expected


def test_get_value_returns_multiple_correct_price():
    given = {"bitcoin": 0.00107096,
             "vertcoin": 0.50628363,
             "ethereum-classic": 0.00283998,
             "zcash": 0.00027895,
             "zcoin": 0.15349718,
             "monacoin": 0.83877923,
             "zencash": 0.00088039,
             "bitcoin-gold": 0.00197191}

    expected = {"bitcoin": 24.29,
                "vertcoin": 5.08,
                "ethereum-classic": 0.11,
                "zcash": 0.17,
                "zcoin": 10.60,
                "monacoin": 15.57,
                "zencash": 0.04,
                "bitcoin-gold": 0.76}
    assets = cs.Crypto_Assets(testing=True)

    assert assets.get_value(given, assets.price) == expected


def test_get_value_returns_str_when_no_price():
    given = {"feathercoin": 1.40910082}
    expected = {"feathercoin": "No price data"}
    assets = cs.Crypto_Assets(testing=True)

    assert assets.get_value(given, assets.price) == expected


def test_get_value_returns_str_for_no_price_when_mixed():
    given = {"bitcoin": 0.00107096,
             "feathercoin": 1.40910082}
    expected = {"bitcoin": 24.29,
                "feathercoin": "No price data"}
    assets = cs.Crypto_Assets(testing=True)

    assert assets.get_value(given, assets.price) == expected


def test_tally_crypto_sums_held_crypto():
    given = {"bitcoin": 24.29,
             "vertcoin": 5.08,
             "ethereum-classic": 0.11,
             "zcash": 0.17,
             "zcoin": 10.60,
             "monacoin": 15.57,
             "zencash": 0.04,
             "bitcoin-gold": 0.76}

    assets = cs.Crypto_Assets(testing=True)

    assert assets.tally_crypto(given) == 56.62


def test_tally_crypto_ingnores_no_data_values():
    given = {"bitcoin": 24.29,
             "vertcoin": 5.08,
             "feathercoin": "No price data",
             "ethereum-classic": 0.11,
             "zcash": 0.17,
             "zclassic": "No price data",
             "zcoin": 10.60,
             "monacoin": 15.57,
             "zencash": 0.04,
             "bitcoin-gold": 0.76}

    assets = cs.Crypto_Assets(testing=True)

    assert assets.tally_crypto(given) == 56.62
