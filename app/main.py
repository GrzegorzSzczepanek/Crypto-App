# from modules.test import StopwatchApp
import modules.data_collection as dc
from TUI_Widgets import coin_ranking as ci
import requests


def make_request(url: str, params: dict = None) -> dict:
    """Make a GET request to the specified URL and interpret the response."""
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == "__main__":
    params = {
        'vs_currency': 'usd',  # The target currency of market data
        # 'ids': 'bitcoin',  # The ids of the coin, comma-separated cryptocurrency symbols
        'order': 'market_cap_desc',  # Sort results by market cap in descending order
        'per_page': 2,  # Total results per page
        'page': 1,  # Page through results
        'sparkline': False,  # Include sparkline 7 days data
        'price_change_percentage': '24h'  # Include price change percentage in 24h
    }

    app = ci.CoinRankingApp()
    app.run()
