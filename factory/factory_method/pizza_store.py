from abc import ABC, abstractmethod
from pizza import Pizza, ChicagoCheesePizza, ChicagoMargheritaPizza
from pizza_enum import PizzaNames


class PizzaStore(ABC):
    def order_pizza(self, pizza_name: PizzaNames) -> Pizza:
        pizza = self.create_pizza(pizza_name)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_name: PizzaNames) -> Pizza:
        """
        A factory method handles object creation and encapsulates it in a subclass.
        This decouples the client code in the superclass from the object creation code in the subclass.
        """
        raise NotImplementedError


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_name: PizzaNames) -> Pizza:
        if pizza_name == PizzaNames.CHEESE:
            print("prepare Chicago style Cheese pizza")
            return ChicagoCheesePizza()
        if pizza_name == PizzaNames.MARGHERITA:
            print("prepare Chicago style Margherita pizza")
            return ChicagoMargheritaPizza()
