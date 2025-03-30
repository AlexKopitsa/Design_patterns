from abc import ABC, abstractmethod

# === Базовий інтерфейс ===
class Beverage(ABC):
    def __init__(self, sugar=0):
        self.sugar = sugar

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def drink(self): pass

    @abstractmethod
    def cost(self): pass

# === Конкретні напої (із задачі) ===
class Coffee(Beverage):
    def prepare(self):
        print("Prepare base coffee...")
        if self.sugar:
            print(f"Add {self.sugar} sugar cubes")

    def drink(self):
        print("Drink coffee!")

    def cost(self):
        return 30

class Tee(Beverage):
    def prepare(self):
        print("Prepare tee...")
        if self.sugar:
            print(f"Add {self.sugar} sugar cubes")

    def drink(self):
        print("Drink tea!")

    def cost(self):
        return 25

class Chocolate(Beverage):
    def prepare(self):
        print("Melt chocolate...")
        if self.sugar:
            print(f"Add {self.sugar} sugar cubes")

    def drink(self):
        print("Drink hot chocolate!")

    def cost(self):
        return 35


# === Абстрактний декоратор ===
class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage

    @abstractmethod
    def prepare(self): pass

    def drink(self):
        self._beverage.drink()

    def cost(self):
        return self._beverage.cost()


# === Декоратори ===
class WithCaramel(BeverageDecorator):
    def prepare(self):
        self._beverage.prepare()
        print("Add caramel...")

    def cost(self):
        return self._beverage.cost() + 5

class WithCream(BeverageDecorator):
    def prepare(self):
        self._beverage.prepare()
        print("Add whipped cream...")

    def cost(self):
        return self._beverage.cost() + 7

class WithSyrup(BeverageDecorator):
    def prepare(self):
        self._beverage.prepare()
        print("Add flavored syrup...")

    def cost(self):
        return self._beverage.cost() + 6


# === Тестування з реальними класами ===
if __name__ == "__main__":
    # Tee with caramel and cream
    tee = Tee(sugar=1)
    decorated_tee = WithCream(WithCaramel(tee))
    print("--- Preparing decorated tea ---")
    decorated_tee.prepare()
    print("--- Drinking ---")
    decorated_tee.drink()
    print(f"Total cost: {decorated_tee.cost()} UAH\n")

    # Chocolate with syrup
    choco = Chocolate(sugar=0)
    decorated_choco = WithSyrup(choco)
    print("--- Preparing decorated chocolate ---")
    decorated_choco.prepare()
    decorated_choco.drink()
    print(f"Total cost: {decorated_choco.cost()} UAH")
