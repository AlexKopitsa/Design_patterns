from abc import ABC, abstractmethod

# === Receiver ===
class Receiver:
    def action(self):
        print("Receiver: Performing the action!")


# === Command (інтерфейс) ===
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# === ConcreteCommand ===
class ConcreteCommand(Command):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    def execute(self):
        print("ConcreteCommand: Executing command...")
        self._receiver.action()


# === Invoker ===
class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command: Command):
        self._command = command

    def invoke(self):
        if self._command:
            print("Invoker: Triggering command execution...")
            self._command.execute()
        else:
            print("Invoker: No command set.")


# === Client ===
if __name__ == "__main__":
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()

    invoker.set_command(command)
    invoker.invoke()
