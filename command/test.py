import door
import light
from command import MacroCommand
from invoker import Remote


def test_remote_client():
    # Receivers
    room_light = light.Light('room')
    garage_light = light.Light('garage')
    garage_door = door.Door('garage', garage_light)

    # Commands
    room_light_on = light.LightOn(room_light)
    room_light_off = light.LightOff(room_light)
    garage_door_open = door.DoorOpen(garage_door)
    garage_door_close = door.DoorClose(garage_door)
    party_on = MacroCommand([room_light_on, garage_door_open])
    party_off = MacroCommand([room_light_off, garage_door_close])

    # Invoker
    capacity = 4
    remote = Remote(capacity)
    remote.set_command(0, room_light_on, room_light_off)
    remote.set_command(1, garage_door_open, garage_door_close)
    remote.set_command(2, party_on, party_off)

    # Execute
    for i in range(capacity):
        print(f'\nbutton number #{i}')
        remote.on_button_was_pushed(i)
        remote.off_button_was_pushed(i)
        remote.undo()

