from effects import Berserk, Blessing, Curse, Weakness, EvilEye
from hero import Hero


def test_decorator():
    hero = Hero()
    hero.get_info()
    hero = EvilEye(Weakness(Curse(Blessing(Berserk(hero)))))
    hero.get_info()
    hero.get_info()
