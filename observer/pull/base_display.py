import interfaces
import weatherdata
from abc import ABC


class BaseDisplay(interfaces.Observer, interfaces.Display, ABC):
    def __init__(self, weather_data: weatherdata.WeatherData):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def __del__(self):
        self.weather_data.remove_observer(self)
