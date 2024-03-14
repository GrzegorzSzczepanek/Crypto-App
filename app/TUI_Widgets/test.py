# from time import monotonic
#
# from textual.app import App, ComposeResult
# from textual.containers import ScrollableContainer
# from textual.reactive import reactive
# from textual.widgets import Button, Footer, Header, Static
#
#
# class TimeDisplay(Static):
#     """A widget to display elapsed time."""
#
#     start_time = reactive(monotonic)
#     time = reactive(0.0)
#     total = reactive(0.0)
#
#     def on_mount(self) -> None:
#         """Event handler called when widget is added to the app."""
#         self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)
#
#     def update_time(self) -> None:
#         """Method to update time to current."""
#         self.time = self.total + (monotonic() - self.start_time)
#
#     def watch_time(self, time: float) -> None:
#         """Called when the time attribute changes."""
#         minutes, seconds = divmod(time, 60)
#         hours, minutes = divmod(minutes, 60)
#         self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")
#
#     def start(self) -> None:
#         """Method to start (or resume) time updating."""
#         self.start_time = monotonic()
#         self.update_timer.resume()
#
#     def stop(self) -> None:
#         """Method to stop the time display updating."""
#         self.update_timer.pause()
#         self.total += monotonic() - self.start_time
#         self.time = self.total
#
#     def reset(self) -> None:
#         """Method to reset the time display to zero."""
#         self.total = 0
#         self.time = 0
#
#
# class Stopwatch(Static):
#     """A stopwatch widget."""
#
#     def on_button_pressed(self, event: Button.Pressed) -> None:
#         """Event handler called when a button is pressed."""
#         button_id = event.button.id
#         time_display = self.query_one(TimeDisplay)
#         if button_id == "start":
#             time_display.start()
#             self.add_class("started")
#         elif button_id == "stop":
#             time_display.stop()
#             self.remove_class("started")
#         elif button_id == "reset":
#             time_display.reset()
#
#     def compose(self) -> ComposeResult:
#         """Create child widgets of a stopwatch."""
#         yield Button("Start", id="start", variant="success")
#         yield Button("Stop", id="stop", variant="error")
#         yield Button("Reset", id="reset")
#         yield TimeDisplay()
#
#
# class StopwatchApp(App):
#     """A Textual app to manage stopwatches."""
#
#     CSS_PATH = "stopwatch03.tcss"
#     BINDINGS = [
#         ("d", "toggle_dark", "Toggle dark mode"),
#         ("q", "exit", "Exit app"),
#         ("r", "remove_stopwatch", "Remove stopwatch"),
#         ("a", "add_stopwatch", "Add stopwatch"),
#     ]
#
#     def compose(self) -> ComposeResult:
#         yield Header()
#         yield Footer()
#         yield ScrollableContainer(Stopwatch(), Stopwatch(), Stopwatch(), id="timers")
#
#     def action_exit(self, event):
#         if event.key == "q":
#             self.exit()
#
#     def action_remove_stopwatch(self) -> None:
#         """An action to remove a stopwatch."""
#         timers = self.query("Stopwatch")
#         if timers:
#             timers.last().remove()
#
#     def action_add_stopwatch(self) -> None:
#         """An action to add a stopwatch."""
#         new_stopwatch = Stopwatch()
#         self.query_one("#timers").mount(new_stopwatch)
#         new_stopwatch.scroll_visible()
#
#     def action_toggle_dark(self) -> None:
#         """An action to toggle dark mode."""
#         self.dark = not self.dark

from textual.app import App
from textual.widgets import Table, Placeholder

class MyApp(App):
    async def on_mount(self) -> None:
        # Create a table with headers
        table = Table(
            [
                ["Name", "Age", "City"],
                ["Alice", 30, "New York"],
                ["Bob", 25, "Los Angeles"],
                ["Charlie", 35, "Chicago"],
            ],
            show_header=True,
            show_lines=True,
        )

        # Add the table to the app
        await self.view.dock(table)

MyApp.run(title="My Table App")

