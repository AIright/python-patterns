from abc import ABC, abstractmethod
from ingredients import (
    Dough, Sauce, Cheese, Vegetable, Pepperoni, Clams,  # abstract classes
    ThinCrustDough, MarinaraSauce, Parmesan,   # concrete ingredients
    Onion, Garlic, RedPepper)


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        raise NotImplementedError

    @abstractmethod
    def create_sauce(self) -> Sauce:
        raise NotImplementedError

    @abstractmethod
    def create_cheese(self) -> Cheese:
        raise NotImplementedError

    @abstractmethod
    def create_veggies(self) -> list[Vegetable]:
        raise NotImplementedError

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        raise NotImplementedError

    @abstractmethod
    def create_clams(self) -> Clams:
        raise NotImplementedError


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return Parmesan()

    def create_veggies(self) -> list[Vegetable]:
        return [Garlic(), Onion(), RedPepper()]

    def create_pepperoni(self) -> Pepperoni:
        return Pepperoni()

    def create_clams(self) -> Clams:
        return Clams()
