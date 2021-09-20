import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class MacroCommand(Command):
    def __init__(self, commands: list[Command]):
        self.commands = commands

    def execute(self):
        for c in self.commands:
            c.execute()

    def undo(self):
        for c in self.commands[::-1]:
            c.undo()


class NoCommand(Command):  # NullObject
    def execute(self):
        print('free slot')

    def undo(self):
        print('free slot')
