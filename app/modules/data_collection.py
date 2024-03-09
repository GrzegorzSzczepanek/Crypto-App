import requests


def interpret_status_code(response: dict) -> dict:
    """Interpret status code."""
    if response.status_code == 200:
        return response.json()
    else:
        return None


def ping_coin_gecko() -> None:
    """Ping CoinGecko API."""
    response = requests.get("https://api.coingecko.com/api/v3/ping")
    print(response.json())


def get_all_token_info_by_id(id: str) -> dict:
    """Get token by id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}")
    return interpret_status_code(response)


def get_supported_vs_currencies() -> dict:
    """Get supported vs currencies."""
    response = requests.get("https://api.coingecko.com/api/v3/simple/supported_vs_currencies")
    return interpret_status_code(response)


def get_simple_price() -> dict:
    """Get simple prive."""
    response = requests.get("https://api.coingecko.com/api/v3/simple/price")
    return interpret_status_code(response)


def get_coins_list() -> dict:
    """Get coins list."""
    response = requests.get("https://api.coingecko.com/api/v3/coins/list")
    return interpret_status_code(response)


def get_coins_markets() -> dict:
    """Get coins markets."""
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets")
    return interpret_status_code(response)


def get_coins_by_id(id: str) -> dict:
    """Get coins by id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}")
    return interpret_status_code(response)


def get_coins_tickers(id: str) -> dict:
    """Get coins tickers."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/tickers")
    return interpret_status_code(response)


def get_coins_history_by_id(id: str) -> dict:
    """Get coins history by id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/market_chart")
    return interpret_status_code(response)


def get_coins_market_charts_by_id(id: str) -> dict:
    """Get coins market charts by id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/market_chart")
    return interpret_status_code(response)


def get_coins_market_charts_range_by_id(id: str) -> dict:
    """Get coins market charts range by id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/market_chart?vs_currency=usd&days=30")
    return interpret_status_code(response)


def get_coins_ohlc_by_id(id: str) -> dict:
    """Get coins ohlc by id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/ohlc")
    return interpret_status_code(response)


def get_coins_info_by_contract_and_id(id: str, contract_address: str) -> dict:
    """Get coins info by contract and id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/contract/{contract_address}")
    return interpret_status_code(response)


def get_market_data_by_id_and_address(id: str, address: str) -> dict:
    """Get market data by id and address."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/contract/{address}/market_chart")
    return interpret_status_code(response)


def get_market_range_data_by_id_and_address(id: str, address: str) -> dict:
    """Get market range data by id and address."""
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/contract/{address}/market_chart/range")
    return interpret_status_code(response)


def get_assets_list() -> dict:
    """Get assets list."""
    response = requests.get("https://api.coingecko.com/api/v3/coins/list")
    return interpret_status_code(response)


def get_categories_list() -> dict:
    """Get categories list."""
    response = requests.get("https://api.coingecko.com/api/v3/coins/categories")
    return interpret_status_code(response)


def get_all_categories_with_market_data() -> dict:
    """Get all categories with market data."""
    response = requests.get("https://api.coingecko.com/api/v3/coins/categories/list")
    return interpret_status_code(response)


def get_exchanges_list() -> dict:
    """Get exchanges list."""
    response = requests.get("https://api.coingecko.com/api/v3/exchanges")
    return interpret_status_code(response)


def get_exchange_by_id(id: str) -> dict:
    """Get exchange by id."""
    response = requests.get(f"https://api.coingecko.com/api/v3/exchanges/{id}")
    return interpret_status_code(response)


def get_exchange_list() -> dict:
    """Get exchange rates."""
    response = requests.get("https://api.coingecko.com/api/v3/exchange/list")
    return interpret_status_code(response)
