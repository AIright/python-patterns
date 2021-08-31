import random
from displays import TemperatureDisplay, FullDataDisplay
from subject import Subject


def test_observer_pattern():
    weather_station = Subject()
    temperature_display = TemperatureDisplay()
    full_data_display = FullDataDisplay()

    weather_station.register_observer(temperature_display)
    weather_station.register_observer(full_data_display)

    for i in range(3):
        weather_station.update_data(
            temperature=random.uniform(10, 30),
            humidity=random.uniform(40, 100),
            pressure=random.uniform(730, 790)
        )

    weather_station.remove_observer(full_data_display)
    for i in range(3):
        weather_station.update_data(
            temperature=random.uniform(10, 30),
            humidity=random.uniform(40, 100),
            pressure=random.uniform(730, 790)
        )
