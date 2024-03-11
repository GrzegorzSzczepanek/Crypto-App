from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static
import modules.data_collection as dc


class CoinRankingHeader(Static):
    """A widget to display header information."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.styles.layout = "horizontal"

    def compose(self) -> ComposeResult:
        """Create child widgets of the header."""
        yield Button("Index", id="index_sort")
        yield Button("Coin", id="coin_sort")
        yield Button("Price", id="price_sort")
        yield Button("24h", id="day_sort")
        yield Button("Volume", id="volume_sort")


class CoinInfo(Static):
    """A widget to display coin information."""

    def __init__(self, market_cap_rank: str, symbol: str, name: str, price: float,
                 one_day_change: float, last_day_volume: float, sparkline: list = None):
        super().__init__()
        self.market_cap_rank = market_cap_rank
        self.symbol = symbol
        self.coin_name = name
        self.price = price
        self.one_day_change = one_day_change
        self.last_day_volume = last_day_volume
        # self.one_hour_change = one_hour_change
        # self.week_change = week_change
        # self.sparkline = sparkline

    def compose(self) -> ComposeResult:
        yield Static(f"{self.market_cap_rank}, {self.symbol}, {self.coin_name}, {self.price}, {self.one_day_change}, {self.last_day_volume}", id="coin_info")


class CoinRankingApp(App):
    """A Textual app to manage coin rankings."""
    BINDINGS = [
        # ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "exit", "Exit app"),
    ]
    CSS_PATH = "styles/coin_ranking.css"

    def compose(self) -> ComposeResult:
        params = {
            'vs_currency': 'usd',  # The target currency of market data
            # 'ids': 'bitcoin',  # The ids of the coin, comma-separated cryptocurrency symbols
            'order': 'market_cap_desc',  # Sort results by market cap in descending order
            'per_page': 10,  # Total results per page
            'page': 1,  # Page through results
            'sparkline': False,  # Include sparkline 7 days data
            'price_change_percentage': '24h'  # Include price change percentage in 24h
        }

        coins = dc.get_coins_markets(params)
        yield CoinRankingHeader(id="header")
        yield Header()
        yield Footer()
        for coin in coins:
            yield CoinInfo(market_cap_rank=coin['market_cap_rank'],
                           symbol=coin['symbol'],
                           name=coin['name'],
                           price=coin['current_price'],
                           one_day_change=coin['price_change_percentage_24h_in_currency'],
                           last_day_volume=coin['total_volume'])

    def action_exit(self, event):
        if event.key == "q":
            self.exit()
