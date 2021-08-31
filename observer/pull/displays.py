from  base_display import BaseDisplay
from weatherdata import WeatherData


class TemperatureDisplay(BaseDisplay):
    def __init__(self, weather_data: WeatherData):
        super(TemperatureDisplay, self).__init__(weather_data)
        self.temperature: float = 0
        self.display()

    def update(self) -> None:
        self.temperature = self.weather_data.temperature
        self.display()

    def display(self) -> None:
        print(f'{self.__class__} - temperature: {self.temperature}')


class FullDataDisplay(BaseDisplay):
    def __init__(self, weather_data: WeatherData):
        super(FullDataDisplay, self).__init__(weather_data)
        self.temperature: float = 0
        self.pressure: float = 0
        self.humidity: float = 0
        self.display()

    def update(self) -> None:
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.pressure = self.weather_data.pressure
        self.display()

    def display(self) -> None:
        print(f'{self.__class__} - temperature: {self.temperature}; '
              f'humidity: {self.humidity}; pressure: {self.pressure}')

