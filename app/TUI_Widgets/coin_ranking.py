from textual.app import App, ComposeResult
# from textual.containers import ScrollableContainer
# from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static
import modules.data_collection as dc
from textual.widget import Widget


class CoinRankingHeader(Widget):
    """A widget to display header information."""

    def on_click(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        if button_id == "index_sort":
            self.variant = "error"
            # Add your logic here for index sorting
            self.add_class("sorted")
        elif button_id == "coin_sort":
            print("Coin sort button clicked")
            # Add your logic here for coin sorting
        elif button_id == "price_sort":
            print("Price sort button clicked")
            # Add your logic here for price sorting
        elif button_id == "day_sort":
            print("24h sort button clicked")
            # Add your logic here for 24h sorting
        elif button_id == "volume_sort":
            print("Volume sort button clicked")
            # Add your logic here for volume sorting

    def compose(self) -> ComposeResult:
        """Create child widgets of the header."""
        yield Button("Index", id="index_sort")
        yield Button("Coin", id="coin_sort")
        yield Button("Price", id="price_sort")
        yield Button("24h Change", id="day_sort")
        yield Button("Today's Volume", id="volume_sort")
        yield Button("Market Cap", id="market_cap_sort")


class CoinInfo(Static):
    """A widget to display coin information."""

    def __init__(self, market_cap_rank: str, symbol: str, name: str, price: float,
                 one_day_change: float, last_day_volume: float, market_cap: float, sparkline: list = None):
        super().__init__()
        self.market_cap_rank = market_cap_rank
        self.symbol = symbol
        self.coin_name = name
        self.price = price
        self.one_day_change = one_day_change
        self.last_day_volume = last_day_volume
        self.market_cap = market_cap
        # self.one_hour_change = one_hour_change
        # self.week_change = week_change
        # self.sparkline = sparkline

    def compose(self) -> ComposeResult:
        """Create child widgets of the coin info."""
        yield Static(str(self.market_cap_rank))
        # yield Static(str(self.symbol))
        yield Static(str(self.coin_name))
        yield Static(str(self.price))
        yield Static(str(self.one_day_change))
        yield Static(str(self.last_day_volume))
        yield Static(str(self.market_cap))


class Coins:
    def __init__(self, params=None):
        self.params = params
        self.coins = dc.get_coins_markets(params)
        print(self.coins)

    def order_by_param(self, order):
        # self.coins = sorted(self.coins, key=lambda x: x[order])
        self.params['order'] = order
        self.coins = dc.get_coins_markets(self.params)


# TODO add sorting functions for each button
class CoinRankingApp(App):
    """A Textual app to manage coin rankings."""
    BINDINGS = [
        # ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "exit", "Exit app"),
    ]
    CSS_PATH = "styles/coin_ranking.tcss"

    def compose(self) -> ComposeResult:
        params = {
            'vs_currency': 'usd',  # The target currency of market data
            # 'ids': 'bitcoin',  # The ids of the coin, comma-separated cryptocurrency symbols
            'order': 'market_cap_desc',  # Sort results by market cap in descending order
            'per_page': 5,  # Total results per page
            'page': 2,  # Page through results
            'sparkline': False,  # Include sparkline 7 days data
            'price_change_percentage': '24h'  # Include price change percentage in 24h
        }

        coins = Coins(params)
        yield CoinRankingHeader(id="header")
        yield Header()
        yield Footer()
        try:
            for coin in coins.coins:
                yield CoinInfo(market_cap_rank=coin['market_cap_rank'],
                               symbol=coin['symbol'],
                               name=coin['name'],
                               price=coin['current_price'],
                               one_day_change=coin['price_change_percentage_24h_in_currency'],
                               last_day_volume=coin['total_volume'],
                               market_cap=coin['market_cap'],
                               )
        except Exception as e:
            print(e)

    def action_exit(self, event):
        if event.key == "q":
            self.exit()
