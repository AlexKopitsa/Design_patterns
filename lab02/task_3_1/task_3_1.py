from abc import ABC, abstractmethod

# Абстрактний продукт (Кава)
class Coffee(ABC):
    def __init__(self, cost_price, sale_price):
        self.cost_price = cost_price  # Собівартість
        self.sale_price = sale_price  # Ціна продажу

    @abstractmethod
    def get_name(self):
        pass

    def get_profit(self):
        return self.sale_price - self.cost_price  # Розрахунок прибутку

# Конкретні продукти (кава)
class Espresso(Coffee):
    def get_name(self):
        return "Еспресо"

class Americano(Coffee):
    def get_name(self):
        return "Американо"

class Cappuccino(Coffee):
    def get_name(self):
        return "Капучіно"

class Latte(Coffee):
    def get_name(self):
        return "Латте"

class Mocha(Coffee):
    def get_name(self):
        return "Мокачино"

class FlatWhite(Coffee):
    def get_name(self):
        return "Флет Вайт"

class RafCoffee(Coffee):
    def get_name(self):
        return "Раф Кава"

# Абстрактна фабрика (творець)
class CoffeeFactory(ABC):
    @abstractmethod
    def create_coffee(self):
        pass

# Конкретні фабрики для кожного виду кави
class EspressoFactory(CoffeeFactory):
    def create_coffee(self):
        return Espresso(cost_price=10, sale_price=25)

class AmericanoFactory(CoffeeFactory):
    def create_coffee(self):
        return Americano(cost_price=12, sale_price=28)

class CappuccinoFactory(CoffeeFactory):
    def create_coffee(self):
        return Cappuccino(cost_price=15, sale_price=35)

class LatteFactory(CoffeeFactory):
    def create_coffee(self):
        return Latte(cost_price=18, sale_price=40)

class MochaFactory(CoffeeFactory):
    def create_coffee(self):
        return Mocha(cost_price=20, sale_price=45)

class FlatWhiteFactory(CoffeeFactory):
    def create_coffee(self):
        return FlatWhite(cost_price=17, sale_price=42)

class RafCoffeeFactory(CoffeeFactory):
    def create_coffee(self):
        return RafCoffee(cost_price=22, sale_price=50)

# Клас кав'ярні
class CoffeeShop:
    def __init__(self):
        self.sales = []

    def sell_coffee(self, factory: CoffeeFactory):
        coffee = factory.create_coffee()
        self.sales.append(coffee)
        print(f"Продано: {coffee.get_name()} за {coffee.sale_price} грн")

    def calculate_total_profit(self):
        return sum(coffee.get_profit() for coffee in self.sales)

# Симуляція роботи кав'ярні з розширеним асортиментом
if __name__ == "__main__":
    shop = CoffeeShop()

    # Продаємо різні види кави
    shop.sell_coffee(EspressoFactory())
    shop.sell_coffee(AmericanoFactory())
    shop.sell_coffee(CappuccinoFactory())
    shop.sell_coffee(LatteFactory())
    shop.sell_coffee(MochaFactory())
    shop.sell_coffee(FlatWhiteFactory())
    shop.sell_coffee(RafCoffeeFactory())
    shop.sell_coffee(RafCoffeeFactory())  # Додатковий продаж

    print(f"Загальний прибуток: {shop.calculate_total_profit()} грн")
