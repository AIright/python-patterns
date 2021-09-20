from command import Command
from light import Light


class Door:
    def __init__(self, name: str, light: Light):
        self.name: str = name
        self.light: Light = light

    def __str__(self):
        return self.name

    def open_door(self):
        print(f'door {self.__str__()} in opening')
        self.light.light_on()

    def close_door(self):
        print(f'door {self.__str__()} in closing')
        self.light.light_off()


class DoorOpen(Command):
    def __init__(self, door: Door):
        self.door: Door = door

    def execute(self):
        self.door.open_door()

    def undo(self):
        self.door.close_door()


class DoorClose(Command):
    def __init__(self, door: Door):
        self.door: Door = door

    def execute(self):
        self.door.close_door()

    def undo(self):
        self.door.open_door()
