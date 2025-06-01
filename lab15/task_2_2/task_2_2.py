from abc import ABC, abstractmethod

# === Receiver ===
class Lamp:
    def turn_on(self):
        print("Lamp is ON")

    def turn_off(self):
        print("Lamp is OFF")


# === Command Interface ===
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# === Concrete Commands ===
class TurnOnCommand(Command):
    def __init__(self, lamp: Lamp):
        self._lamp = lamp

    def execute(self):
        self._lamp.turn_on()

class TurnOffCommand(Command):
    def __init__(self, lamp: Lamp):
        self._lamp = lamp

    def execute(self):
        self._lamp.turn_off()


# === Invoker ===
class Controller:
    def __init__(self):
        self._on_command = None
        self._off_command = None

    def set_commands(self, on_command: Command, off_command: Command):
        self._on_command = on_command
        self._off_command = off_command

    def press_on_button(self):
        print("[Controller] ON button pressed")
        self._on_command.execute()

    def press_off_button(self):
        print("[Controller] OFF button pressed")
        self._off_command.execute()


# === Client ===
if __name__ == "__main__":
    lamp = Lamp()
    turn_on = TurnOnCommand(lamp)
    turn_off = TurnOffCommand(lamp)

    controller = Controller()
    controller.set_commands(turn_on, turn_off)

    controller.press_on_button()
    controller.press_off_button()
