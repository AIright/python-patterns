from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def quack(self):
        pass


class NoQuack(QuackBehavior):
    def quack(self):
        print('this duck cannot quack!')


class BarkQuack(QuackBehavior):
    def quack(self):
        print('this duck barks! wtf?!')


class QuackQuack(QuackBehavior):
    def quack(self):
        print('quack!')
