from abc import ABC, abstractmethod
import pizza
from ingredient_factory import NYPizzaIngredientFactory
from pizza_enum import PizzaNames


class PizzaStore(ABC):
    def order_pizza(self, pizza_name: PizzaNames) -> pizza.Pizza:
        order = self.create_pizza(pizza_name)

        order.prepare()
        order.bake()
        order.cut()
        order.box()

        return order

    @abstractmethod
    def create_pizza(self, pizza_name: PizzaNames) -> pizza.Pizza:
        """
        A factory method handles object creation and encapsulates it in a subclass.
        This decouples the client code in the superclass from the object creation code in the subclass.
        """
        raise NotImplementedError


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_name: PizzaNames) -> pizza.Pizza:
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_name == PizzaNames.CHEESE:
            print("prepare New York style Cheese pizza")
            return pizza.CheesePizza(ingredient_factory)

        if pizza_name == PizzaNames.MARGHERITA:
            print("prepare New York style Margherita pizza")
            return pizza.MargheritaPizza(ingredient_factory)
