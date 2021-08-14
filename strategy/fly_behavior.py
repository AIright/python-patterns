from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class NoFly(FlyBehavior):
    def fly(self):
        print('this duck cannot fly!')


class RocketFly(FlyBehavior):
    def fly(self):
        print('this duck flies like a rocket!')


class FlyWithWings(FlyBehavior):
    def fly(self):
        print('this duck uses its wings to fly!')
