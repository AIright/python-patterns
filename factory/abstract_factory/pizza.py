from abc import ABC, abstractmethod
from ingredients import Dough, Sauce, Cheese, Vegetable, Pepperoni, Clams
from ingredient_factory import PizzaIngredientFactory
from pizza_enum import PizzaNames


class Pizza(ABC):
    name: str
    dough: Dough
    sauce: Sauce
    cheese: Cheese
    veggies: list[Vegetable]
    pepperoni: Pepperoni
    clams: Clams

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredients = ingredient_factory

    @abstractmethod
    def prepare(self):
        """
        The Abstract Factory Pattern provides an interface for creating families of related or
        dependent objects without specifying their concrete classes.
        Abstract Factory allows a client to use an abstract interface to create a set of related products
        without knowing (or caring) about the concrete products that are actually produced.
        In this way, the client is decoupled from any of the specifics of the concrete products.
        """
        raise NotImplementedError

    def bake(self):
        print(f"cooking {self.name}")

    def cut(self):
        print(f"slicing {self.name}")

    def box(self):
        print(f"packing {self.name}")


class CheesePizza(Pizza):
    name = PizzaNames.CHEESE

    def prepare(self):
        self.dough = self.ingredients.create_dough()
        self.sauce = self.ingredients.create_sauce()
        self.cheese = self.ingredients.create_cheese()
        print(f'{self.name.value} pizza ingredients: {self.__dict__}')


class MargheritaPizza(Pizza):
    name = PizzaNames.MARGHERITA

    def prepare(self):
        self.dough = self.ingredients.create_dough()
        self.sauce = self.ingredients.create_sauce()
        self.cheese = self.ingredients.create_cheese()
        self.veggies = self.ingredients.create_veggies()
        print(f'{self.name.value} pizza ingredients: {self.__dict__}')
