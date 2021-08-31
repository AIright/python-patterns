import interfaces


class WeatherData(interfaces.Subject):
    def __init__(self):
        super(WeatherData, self).__init__()
        self._temperature: float = 0
        self._pressure: float = 0
        self._humidity: float = 0

    def update_data(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()  # notify observers with every change in data

    @property
    def temperature(self):
        return self._temperature

    @property
    def pressure(self):
        return self._pressure

    @property
    def humidity(self):
        return self._humidity
