from abc import ABC, abstractmethod

# === Базовий клас напою ===
class Beverage(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    def __str__(self):
        return f"Beverage: {self.description()}, ${self.cost():.2f}"

# === Конкретні напої ===
class Espresso(Beverage):
    def description(self):
        return "Espresso"

    def cost(self):
        return 0.75

class DarkRoast(Beverage):
    def description(self):
        return "Dark Roast"

    def cost(self):
        return 1.00

class Decaf(Beverage):
    def description(self):
        return "Decaf"

    def cost(self):
        return 0.50

# === Абстрактний декоратор ===
class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

# === Декоратори (додатки) ===
class Milk(CondimentDecorator):
    def description(self):
        return self._beverage.description() + ", milk"

    def cost(self):
        return self._beverage.cost() + 0.20

class Chocolate(CondimentDecorator):
    def description(self):
        return self._beverage.description() + ", chocolate"

    def cost(self):
        return self._beverage.cost() + 0.30

class Cream(CondimentDecorator):
    def description(self):
        return self._beverage.description() + ", cream"

    def cost(self):
        return self._beverage.cost() + 0.15

# === Тестування ===
if __name__ == "__main__":
    espresso = Espresso()
    print(espresso)

    dark = DarkRoast()
    dark_with_milk = Milk(dark)
    dark_with_chocolate = Chocolate(dark_with_milk)
    dark_full = Cream(dark_with_chocolate)
    print(dark_full)

    decaf = Cream(Milk(Decaf()))
    print(decaf)