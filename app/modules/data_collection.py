import requests
# beta features of coingecko are unincluded


def make_request(url: str, params: dict = None) -> dict:
    """Make a GET request to the specified URL and interpret the response."""
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def ping_coin_gecko(params: dict = None) -> None:
    """Ping CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/ping"
    return make_request(url, params)


def get_all_token_info_by_id(id: str, params: dict = None) -> dict:
    """Get token by id."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}"
    return make_request(url, params)


def get_supported_vs_currencies(params: dict = None) -> dict:
    """Get supported vs currencies."""
    url = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
    return make_request(url, params)


def get_simple_price(params: dict = None) -> dict:
    """Get simple prive."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    return make_request(url, params)


def get_coins_list(params: dict = None) -> dict:
    """Get coins list."""
    url = "https://api.coingecko.com/api/v3/coins/list"
    return make_request(url, params)


def get_coins_markets(params: dict = None) -> dict:
    """Get coins markets."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    return make_request(url, params)


def get_coins_by_id(id: str, params: dict = None) -> dict:
    """Get coins by id."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}"
    return make_request(url, params)


def get_coins_tickers(id: str, params: dict = None) -> dict:
    """Get coins tickers."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/tickers"
    return make_request(url, params)


def get_coins_history_by_id(id: str, params: dict = None) -> dict:
    """Get coins history by id."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
    return make_request(url, params)


def get_coins_market_charts_by_id(id: str, params: dict = None) -> dict:
    """Get coins market charts by id."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
    return make_request(url, params)


def get_coins_market_charts_range_by_id(id: str, params: dict = None) -> dict:
    """Get coins market charts range by id."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart?vs_currency=usd&days=30"
    return make_request(url, params)


def get_coins_ohlc_by_id(id: str, params: dict = None) -> dict:
    """Get coins ohlc by id."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/ohlc"
    return make_request(url, params)


def get_coins_info_by_contract_and_id(id: str, contract_address: str, params: dict = None) -> dict:
    """Get coins info by contract and id."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/contract/{contract_address}"
    return make_request(url, params)


def get_market_data_by_id_and_address(id: str, address: str, params: dict = None) -> dict:
    """Get market data by id and address."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/contract/{address}/market_chart"
    return make_request(url, params)


def get_market_range_data_by_id_and_address(id: str, address: str, params: dict = None) -> dict:
    """Get market range data by id and address."""
    url = f"https://api.coingecko.com/api/v3/coins/{id}/contract/{address}/market_chart/range"
    return make_request(url, params)


def get_assets_list(params: dict = None) -> dict:
    """Get assets list."""
    url = "https://api.coingecko.com/api/v3/coins/list"
    return make_request(url, params)


def get_categories_list(params: dict = None) -> dict:
    """Get categories list."""
    url = "https://api.coingecko.com/api/v3/coins/categories"
    return make_request(url, params)


def get_all_categories_with_market_data(params: dict = None) -> dict:
    """Get all categories with market data."""
    url = "https://api.coingecko.com/api/v3/coins/categories/list"
    return make_request(url, params)


def get_exchanges_list(params: dict = None) -> dict:
    """Get exchanges list."""
    url = "https://api.coingecko.com/api/v3/exchanges"
    return make_request(url, params)


def get_exchange_by_id(id: str, params: dict = None) -> dict:
    """Get exchange by id."""
    url = f"https://api.coingecko.com/api/v3/exchanges/{id}"
    return make_request(url, params)


def get_exchanges_tickers_by_id(id: str, params: dict = None) -> dict:
    """Get exchange tickers by id."""
    url = f"https://api.coingecko.com/api/v3/exchanges/{id}/tickers"
    return make_request(url, params)


def get_exchanges_volume_by_id(id: str, params: dict = None) -> dict:
    """Get exchange volume by id."""
    url = f"https://api.coingecko.com/api/v3/exchanges/{id}/volume_chart"
    return make_request(url, params)


def get_derivatives(params: dict = None) -> dict:
    """Get all derivatives tickers"""
    url = "https://api.coingecko.com/api/v3/derivatives"
    return make_request(url, params)


def get_derivatices_exchanges(params: dict = None) -> dict:
    """Get all derivatives exchanges"""
    url = "https://api.coingecko.com/api/v3/derivatives/exchanges"
    return make_request(url, params)


def get_derivatives_exchange_by_id(id: str, params: dict = None) -> dict:
    """Get derivatives exchange by id."""
    url = f"https://api.coingecko.com/api/v3/derivatives/exchanges/{id}"
    return make_request(url, params)


def get_derivatives_exchange_list(params: dict = None) -> dict:
    """Get derivatives exchange list."""
    url = "https://api.coingecko.com/api/v3/derivatives/exchanges/list"
    return make_request(url, params)


def get_exchange_rates(params: dict = None) -> dict:
    """Get exchange rates."""
    url = "https://api.coingecko.com/api/v3/exchange_rates"
    return make_request(url, params)


def search(query: str, params: dict = None) -> dict:
    """Search for coins, categories and markets on CoinGecko."""
    url = f"https://api.coingecko.com/api/v3/search?query={query}"
    return make_request(url, params)


def search_trending(params: dict = None) -> dict:
    """Get trending search coins (Top-7) on CoinGecko in the last 24 hours"""
    url = "https://api.coingecko.com/api/v3/search/trending"
    return make_request(url, params)


def get_global_data(params: dict = None) -> dict:
    """Get global data."""
    url = "https://api.coingecko.com/api/v3/global"
    return make_request(url, params)


def get_global_defi_data(params: dict = None) -> dict:
    """Get global defi data."""
    url = "https://api.coingecko.com/api/v3/global/decentralized_finance_defi"
    return make_request(url, params)
