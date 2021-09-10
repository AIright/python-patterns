from pizza_enum import PizzaNames
from pizza_store import ChicagoPizzaStore


def test_pizza_store():
    store = ChicagoPizzaStore()
    store.order_pizza(PizzaNames.CHEESE)
    store.order_pizza(PizzaNames.MARGHERITA)
