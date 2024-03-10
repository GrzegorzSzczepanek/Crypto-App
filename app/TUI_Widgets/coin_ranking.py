from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static

"""
[{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400', 'current_price': 69418, 'market_cap': 13633553619
76, 'market_cap_rank': 1, 'fully_diluted_valuation': 1456979772048, 'total_volume': 32017820973, 'high_24h': 70009, 'low_24h': 68351, 'price_change_24h': 928.17, 'price_change_percentage_24
h': 1.35518, 'market_cap_change_24h': 17413802075, 'market_cap_change_percentage_24h': 1.2938, 'circulating_supply': 19650556.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath':
 70009, 'ath_change_percentage': -0.85504, 'ath_date': '2024-03-10T10:25:12.902Z', 'atl': 67.81, 'atl_change_percentage': 102260.97136, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None,
'last_updated': '2024-03-10T20:59:49.544Z', 'price_change_percentage_24h_in_currency': 1.3551847160457453}]

"""


class CoinRankingHeader(Static):
    """A widget to display header information."""

    def compose(self) -> ComposeResult:
        yield "CoinRanking"


class CoinInfo(Static):
    """A widget to display coin information."""

    def __init__(self, id: str, symbol: str, name: str, price: float, one_hour_change: float,
                 one_day_change: float, week_change: float, last_day_volume: float, sparkline: list):
        super().__init__()
        self.id = id
        self.symbol = symbol
        self.price = price
        self.one_hour_change = one_hour_change
        self.one_day_change = one_day_change
        self.week_change = week_change
        self.last_day_volume = last_day_volume
        self.sparkline = sparkline

    def compose(self) -> ComposeResult:
        yield Static(f"{self.symbol}: {self.id}")


class CoinRankingWidget(App):
    """A Textual app to manage coin rankings."""
    # BINDINGS = [
    #     ("d", "toggle_dark", "Toggle dark mode"),
    #     ("q", "exit", "Exit app"),
    # ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(CoinInfo(id="bitcoin", symbol="btc", name="Bitcoin", price=69418, one_hour_change=928.17, one_day_change=928.17, week_change=928.17, last_day_volume=32017820973, sparkline=[]), id="coin_info")

    # def action_exit(self, event):
    #     if event.key == "q":
    #         self.exit()
