from abc import ABC, abstractmethod
# interfaces are required to get rid of circular dependency


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class Display(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class Subject:
    def __init__(self):
        self.observers: set[Observer] = set()

    def register_observer(self, observer: Observer) -> None:
        self.observers.add(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update()
