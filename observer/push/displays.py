from observer import Observer
from subject import Subject


class TemperatureDisplay(Observer):
    def __init__(self):
        self.temperature: float = 0
        self.display()

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.display()

    def display(self) -> None:
        print(f'{self.__class__} - temperature: {self.temperature}')


class FullDataDisplay(Observer):
    def __init__(self):
        self.temperature: float = 0
        self.pressure: float = 0
        self.humidity: float = 0
        self.display()

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self) -> None:
        print(f'{self.__class__} - temperature: {self.temperature}; '
              f'humidity: {self.humidity}; pressure: {self.pressure}')

