# The pattern is called "Strategy" while the way we use polymorphism to encapsulate behaviors is called "Composition"
# Principle 1: Favor composition over inheritance
from abc import ABC

from fly_behavior import FlyBehavior, NoFly, RocketFly
from quack_behavior import QuackBehavior, NoQuack, BarkQuack


class Duck(ABC):
    def __init__(self, quack_behavior: QuackBehavior, fly_behavior: FlyBehavior):
        # Accepts instances of QuackBehavior and FlyBehavior
        self.__quack_behavior = quack_behavior
        self.__fly_behavior = fly_behavior
        self.name = type(self)

    def swim(self):
        print(f'duck {self.name} is swimming')

    def display(self):
        print(f'duck {self.name} looks gorgeous')

    def perform_fly(self):
        self.__fly_behavior.fly()

    def perform_quack(self):
        self.__quack_behavior.quack()

    # Setter allows to set the behavior dynamically
    def __set_quack_behaviour(self, quack_behavior: QuackBehavior):
        self.__quack_behavior = quack_behavior

    def __set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.__fly_behavior = fly_behavior

    # Need to define properties that way instead of @property in order to create a property with setters only
    fly_behavior = property(fset=__set_fly_behavior)
    quack_behaviour = property(fset=__set_quack_behaviour)


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(quack_behavior=NoQuack(), fly_behavior=NoFly())


class RocketDuck(Duck):
    def __init__(self):
        super().__init__(quack_behavior=BarkQuack(), fly_behavior=RocketFly())
