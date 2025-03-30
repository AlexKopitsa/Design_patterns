from abc import ABC, abstractmethod

# === Інтерфейс Printable ===
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

# === Базовий PrintableString ===
class PrintableString(Printable):
    def __init__(self, base: str):
        self.base = base

    def print(self):
        print(self.base, end="")

# === Абстрактний декоратор ===
class PrintableDecorator(Printable):
    def __init__(self, wrapped: Printable):
        self._wrapped = wrapped

    @abstractmethod
    def print(self):
        pass

# === Конкретні декоратори ===
class QuotesDecorator(PrintableDecorator):
    def print(self):
        print('"', end="")
        self._wrapped.print()
        print('"', end="")

class BracketsDecorator(PrintableDecorator):
    def print(self):
        print('[', end="")
        self._wrapped.print()
        print(']', end="")

class NewlineDecorator(PrintableDecorator):
    def print(self):
        self._wrapped.print()
        print()  # new line

# === Тестування ===
if __name__ == "__main__":
    base = PrintableString("Hello, World!")
    decorated = NewlineDecorator(QuotesDecorator(BracketsDecorator(base)))
    decorated.print()  # Виведе: "[Hello, World!]"\n