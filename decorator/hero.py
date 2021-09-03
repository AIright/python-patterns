class Hero:
    def __init__(self):
        self.positive_effects: list[str] = []
        self.negative_effects: list[str] = []

        self.stats: dict[str, int] = {
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
        return self.positive_effects.copy()  # if we return pointer on original stats they will be changed by decorator

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

    def get_info(self):
        print(f'positive effects: {self.get_positive_effects()}')
        print(f'negative effects: {self.get_negative_effects()}')
        print(f'stats: {self.get_stats()}')
