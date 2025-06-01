from abc import ABC, abstractmethod

# === Receiver ===
class Lamp:
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
    def __init__(self, lamp: Lamp):
        self._lamp = lamp

    def execute(self):
        self._lamp.turn_on()


class TurnOffCommand(Command):
    def __init__(self, lamp: Lamp):
        self._lamp = lamp

    def execute(self):
        self._lamp.turn_off()


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
    lamp3 = Lamp("Lamp 3")
    doc = Document()

    on1 = TurnOnCommand(lamp1)
    off1 = TurnOffCommand(lamp1)
    on2 = TurnOnCommand(lamp2)
    off2 = TurnOffCommand(lamp2)
    on3 = TurnOnCommand(lamp3)
    off3 = TurnOffCommand(lamp3)
    create_cmd = CreateDocumentCommand(doc)
    save_cmd = SaveDocumentCommand(doc)
    print_cmd = PrintDocumentCommand(doc)

    controller = Controller()
    controller.set_command("on1", on1)
    controller.set_command("off1", off1)
    controller.set_command("on2", on2)
    controller.set_command("off2", off2)
    controller.set_command("on3", on3)
    controller.set_command("off3", off3)
    controller.set_command("create", create_cmd)
    controller.set_command("save", save_cmd)
    controller.set_command("print", print_cmd)

    controller.press_button("on1")
    controller.press_button("on2")
    controller.press_button("on3")

    controller.press_all_off()

    controller.press_button("create")
    controller.press_button("save")
    controller.press_button("print")
