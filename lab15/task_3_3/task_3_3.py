from abc import ABC, abstractmethod

# === Receiver Interfaces ===
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# === Concrete Devices ===
class Lamp(Device):
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name} is ON")

    def turn_off(self):
        print(f"{self.name} is OFF")

class Television(Device):
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name} is ON")

    def turn_off(self):
        print(f"{self.name} is OFF")


class Document:
    def create(self):
        print("Document created")

    def save(self):
        print("Document saved")

    def print_file(self):
        print("Document sent to printer")


# === Command Interface ===
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# === Concrete Commands ===
class TurnOnCommand(Command):
    def __init__(self, device: Device):
        self._device = device

    def execute(self):
        self._device.turn_on()


class TurnOffCommand(Command):
    def __init__(self, device: Device):
        self._device = device

    def execute(self):
        self._device.turn_off()


class CreateDocumentCommand(Command):
    def __init__(self, doc: Document):
        self._doc = doc

    def execute(self):
        self._doc.create()


class SaveDocumentCommand(Command):
    def __init__(self, doc: Document):
        self._doc = doc

    def execute(self):
        self._doc.save()


class PrintDocumentCommand(Command):
    def __init__(self, doc: Document):
        self._doc = doc

    def execute(self):
        self._doc.print_file()


# === Invoker ===
class Controller:
    def __init__(self):
        self._commands = {}

    def set_command(self, name: str, command: Command):
        self._commands[name] = command

    def press_button(self, name: str):
        if name in self._commands:
            print(f"[Controller] {name} button pressed")
            self._commands[name].execute()
        else:
            print(f"[Controller] No command bound to '{name}'")

    def press_all_off(self):
        print("[Controller] ALL OFF button pressed")
        for name, command in self._commands.items():
            if isinstance(command, TurnOffCommand):
                command.execute()


# === Client ===
if __name__ == "__main__":
    lamp1 = Lamp("Lamp 1")
    lamp2 = Lamp("Lamp 2")
    tv = Television("TV 1")
    doc = Document()

    controller = Controller()

    # Lamps
    controller.set_command("on_lamp1", TurnOnCommand(lamp1))
    controller.set_command("off_lamp1", TurnOffCommand(lamp1))
    controller.set_command("on_lamp2", TurnOnCommand(lamp2))
    controller.set_command("off_lamp2", TurnOffCommand(lamp2))

    # TV
    controller.set_command("on_tv", TurnOnCommand(tv))
    controller.set_command("off_tv", TurnOffCommand(tv))

    # Document
    controller.set_command("create", CreateDocumentCommand(doc))
    controller.set_command("save", SaveDocumentCommand(doc))
    controller.set_command("print", PrintDocumentCommand(doc))

    controller.press_button("on_lamp1")
    controller.press_button("on_tv")

    controller.press_all_off()

    controller.press_button("create")
    controller.press_button("save")
    controller.press_button("print")
