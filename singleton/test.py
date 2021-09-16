from chocolate_factory import ChocolateFactory


def test_chocolate_factory():
    factory_1 = ChocolateFactory()
    factory_2 = ChocolateFactory()
    assert factory_1 is factory_2
