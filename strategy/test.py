import pytest

from duck import RubberDuck, RocketDuck
from fly_behavior import FlyWithWings
from quack_behavior import QuackQuack


@pytest.mark.parametrize('duck', [RubberDuck(), RocketDuck()])
def test_ducks(duck):
    duck.swim()
    duck.display()
    duck.perform_quack()
    duck.perform_fly()

    duck.quack_behaviour = QuackQuack()
    duck.fly_behavior = FlyWithWings()

    duck.perform_quack()
    duck.perform_fly()
