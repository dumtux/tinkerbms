from textual.app import App
from textual.widgets import Header, Footer, Static
from textual.reactive import reactive

class BMSMonitorApp(App):
    voltage = reactive(48.0)
    current = reactive(10.0)
    temperature = reactive(25.0)

    def compose(self):
        yield Header()
        yield Static(f"Voltage: {self.voltage}V", id="voltage")
        yield Static(f"Current: {self.current}A", id="current")
        yield Static(f"Temperature: {self.temperature}°C", id="temperature")
        yield Footer()

    async def on_mount(self):
        # Simulate updating values
        self.set_interval(1, self.update_values)

    async def update_values(self):
        self.voltage = round(self.voltage + 0.1, 2)
        self.current = round(self.current + 0.1, 2)
        self.temperature = round(self.temperature + 0.1, 2)
        self.query_one("#voltage").update(f"Voltage: {self.voltage}V")
        self.query_one("#current").update(f"Current: {self.current}A")
        self.query_one("#temperature").update(f"Temperature: {self.temperature}°C")


if __name__ == "__main__":
    BMSMonitorApp().run()
