from abc import ABC
from observer import Observer


class Subject(ABC):
    def __init__(self):
        self.temperature: float = 0
        self.pressure: float = 0
        self.humidity: float = 0
        self.observers: set[Observer] = set()

    def register_observer(self, observer: Observer) -> None:
        self.observers.add(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(
                temperature=self.temperature,
                humidity=self.humidity,
                pressure=self.pressure
            )

    def update_data(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()  # notify observers with every change in data
