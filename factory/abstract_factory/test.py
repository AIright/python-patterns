from pizza_enum import PizzaNames
from pizza_store import NYPizzaStore


def test_pizza_factory():
    store = NYPizzaStore()
    store.order_pizza(PizzaNames.CHEESE)
    store.order_pizza(PizzaNames.MARGHERITA)
