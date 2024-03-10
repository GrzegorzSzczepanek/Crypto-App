# from modules.test import StopwatchApp
import modules.data_collection as dc
from TUI_Widgets import coin_ranking as ci

if __name__ == "__main__":
    params = {
        'vs_currency': 'usd',  # The target currency of market data
        # 'ids': 'bitcoin',  # The ids of the coin, comma-separated cryptocurrency symbols
        'order': 'market_cap_desc',  # Sort results by market cap in descending order
        'per_page': 2,  # Total results per page
        'page': 1,  # Page through results
        'sparkline': False,  # Include sparkline 7 days data
        'price_change_percentage': ['1h', '24h', '7d']  # Include price change percentage in 24h
    }
    print(dc.get_coins_markets(params))

    # app = ci.CoinRankingWidget()
    # app.run()
