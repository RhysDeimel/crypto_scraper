from crypto_scraper import coinpool


class TestMiningPoolHub:

    def test_fetch_raw_data_default_url_is_valid(self):
        pool = coinpool.MiningPoolHub()
        assert "getuserallbalances" in pool.fetch_raw_data().keys()

    def test_miningpoolhub_api_version_has_not_changed(self):
        pool = coinpool.MiningPoolHub()
        api_version = pool.fetch_raw_data()['getuserallbalances']['version']
        assert api_version == "1.0.0"
