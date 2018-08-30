from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

    def get_info(self):
        print(self.get_positive_effects())
        print(self.get_negative_effects())
        print(self.get_stats())


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
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
        tempo = self.base.get_positive_effects()
        tempo.append(self.__class__.__name__)
        return tempo

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
        tempo = self.base.get_negative_effects()
        tempo.append(self.__class__.__name__)
        return tempo


class Berserk(AbstractPositive):
    def get_stats(self):
        tempo = self.base.get_stats()
        tempo["Strength"] += 7
        tempo["Endurance"] += 7
        tempo["Agility"] += 7
        tempo["Luck"] += 7
        tempo["HP"] += 50
        tempo["Perception"] -= 3
        tempo["Intelligence"] -= 3
        tempo["Charisma"] -= 3
        return tempo


class Blessing(AbstractPositive):
    def get_stats(self):
        tempo = self.base.get_stats()
        tempo["Strength"] += 2
        tempo["Endurance"] += 2
        tempo["Agility"] += 2
        tempo["Luck"] += 2
        tempo["Perception"] += 2
        tempo["Intelligence"] += 2
        tempo["Charisma"] += 2
        return tempo


class Weakness(AbstractNegative):
    def get_stats(self):
        tempo = self.base.get_stats()
        tempo["Strength"] -= 4
        tempo["Endurance"] -= 4
        tempo["Agility"] -= 4
        return tempo


class EvilEye(AbstractNegative):
    def get_stats(self):
        tempo = self.base.get_stats()
        tempo["Luck"] -= 10
        return tempo


class Curse(AbstractNegative):
    def get_stats(self):
        tempo = self.base.get_stats()
        tempo["Strength"] -= 2
        tempo["Endurance"] -= 2
        tempo["Agility"] -= 2
        tempo["Luck"] -= 2
        tempo["Perception"] -= 2
        tempo["Intelligence"] -= 2
        tempo["Charisma"] -= 2
        return tempo


hero = Hero()
hero.get_info()
bers = Berserk(hero)
bers.get_info()