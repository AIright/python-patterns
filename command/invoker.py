from command import Command, NoCommand


no_command = NoCommand()
# NullObject pattern is here.
# It is used when we don't have anything to return
# and to remove the responsibility from the client to handle None value


class Remote:
    def __init__(self, capacity):
        self.capacity = capacity
        self.on_commands: list[Command] = [no_command for _ in range(0, self.capacity)]  # NullObject
        self.off_commands: list[Command] = [no_command for _ in range(0, self.capacity)]  # NullObject
        self.recent_command: Command = no_command  # NullObject

    def set_command(self, position: int, on_command: Command, off_command: Command):
        self.on_commands[position] = on_command
        self.off_commands[position] = off_command

    def on_button_was_pushed(self, position: int):
        self.on_commands[position].execute()
        self.recent_command = self.on_commands[position]

    def off_button_was_pushed(self, position: int):
        self.off_commands[position].execute()
        self.recent_command = self.off_commands[position]

    def undo(self):
        self.recent_command.undo()
