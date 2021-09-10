from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


class ChicagoCheesePizza(Pizza):
    def prepare(self):
        print("Chicago cheese: prepare")

    def bake(self):
        print("Chicago cheese: bake")

    def cut(self):
        print("Chicago cheese: cut")

    def box(self):
        print("Chicago cheese: box")


class ChicagoMargheritaPizza(Pizza):
    def prepare(self):
        print("Chicago Margherita: prepare")

    def bake(self):
        print("Chicago Margherita: bake")

    def cut(self):
        print("Chicago Margherita: cut")

    def box(self):
        print("Chicago Margherita: box")
