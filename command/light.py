from command import Command


class Light:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return self.name

    def light_on(self):
        print(f'light {self.__str__()} is on')

    def light_off(self):
        print(f'light {self.__str__()} is off')


class LightOn(Command):
    def __init__(self, light: Light):
        self.light: Light = light

    def execute(self):
        self.light.light_on()

    def undo(self):
        self.light.light_off()


class LightOff(Command):
    def __init__(self, light: Light):
        self.light: Light = light

    def execute(self):
        self.light.light_off()

    def undo(self):
        self.light.light_on()
