from abc import ABC, abstractmethod
from hero import Hero


class AbstractEffect(Hero, ABC):
    """
    Decorator = decorated object child + composition (HAS-A) of ancestor
    class AbstractEffect(Hero)
    h = AbstractEffect(Hero())  - this hero is decorated with AbstractEffect
    """
    def __init__(self, base: Hero):
        super().__init__()
        self.base = base

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect, ABC):
    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append(self.__class__.__name__)
        return effects

    @abstractmethod
    def get_stats(self):
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect, ABC):
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_stats(self):
        pass

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append(self.__class__.__name__)
        return effects
