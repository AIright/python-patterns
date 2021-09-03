from decorator import AbstractPositive, AbstractNegative


class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["HP"] += 50
        stats["Perception"] -= 3
        stats["Intelligence"] -= 3
        stats["Charisma"] -= 3
        return stats


class Blessing(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Intelligence"] += 2
        stats["Charisma"] += 2
        return stats


class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats


class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats


class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Intelligence"] -= 2
        stats["Charisma"] -= 2
        return stats
