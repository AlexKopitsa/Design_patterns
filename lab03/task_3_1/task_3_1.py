from abc import ABC, abstractmethod

# Абстрактний клас для кавових машин
class CoffeeMachine(ABC):
    def __init__(self, machine_cost, maintenance_cost_per_day):
        self.machine_cost = machine_cost  # Вартість кавомашини
        self.maintenance_cost_per_day = maintenance_cost_per_day  # Витрати на обслуговування

    @abstractmethod
    def make_coffee(self):
        pass

    def get_total_cost(self, days):
        """Загальні витрати на кавову машину та обслуговування за N днів."""
        return self.machine_cost + (self.maintenance_cost_per_day * days)


# Конкретні кавові машини
class DeLonghiMachine(CoffeeMachine):
    def make_coffee(self):
        return "Еспресо, Американо"

class PhilipsMachine(CoffeeMachine):
    def make_coffee(self):
        return "Латте, Капучіно"

class JuraMachine(CoffeeMachine):
    def make_coffee(self):
        return "Мокачино, Флет Вайт"


# Абстрактна фабрика кавових машин
class CoffeeMachineFactory(ABC):
    @abstractmethod
    def create_machine(self):
        pass


# Конкретні фабрики виробників кавових машин
class DeLonghiFactory(CoffeeMachineFactory):
    def create_machine(self):
        return DeLonghiMachine(machine_cost=50_000, maintenance_cost_per_day=150)

class PhilipsFactory(CoffeeMachineFactory):
    def create_machine(self):
        return PhilipsMachine(machine_cost=60_000, maintenance_cost_per_day=130)

class JuraFactory(CoffeeMachineFactory):
    def create_machine(self):
        return JuraMachine(machine_cost=70_000, maintenance_cost_per_day=120)


# Клас для розрахунку прибутку кав'ярні
class CoffeeShop:
    def __init__(self, coffee_prices, coffee_costs, daily_sales, days):
        self.coffee_prices = coffee_prices  # Вартість продажу напоїв
        self.coffee_costs = coffee_costs  # Собівартість напоїв
        self.daily_sales = daily_sales  # Продажі кожного напою за день
        self.days = days  # Загальна кількість днів роботи

    def calculate_profit(self, machine):
        """Розрахунок прибутку для кавової машини."""
        total_income = 0

        # Отримуємо список напоїв, які готує машина
        available_coffees = machine.make_coffee().split(", ")

        for coffee in available_coffees:
            if coffee in self.coffee_prices:
                total_income += (self.coffee_prices[coffee] - self.coffee_costs[coffee]) * self.daily_sales[coffee] * self.days

        total_expenses = machine.get_total_cost(self.days)
        return total_income - total_expenses


# Вхідні дані
coffee_prices = {
    "Еспресо": 50, "Американо": 55,
    "Латте": 65, "Капучіно": 70,
    "Мокачино": 75, "Флет Вайт": 80
}

coffee_costs = {
    "Еспресо": 20, "Американо": 25,
    "Латте": 30, "Капучіно": 35,
    "Мокачино": 40, "Флет Вайт": 45
}

daily_sales = {
    "Еспресо": 40, "Американо": 35,
    "Латте": 30, "Капучіно": 25,
    "Мокачино": 20, "Флет Вайт": 15
}

days = 90  # Кав'ярня працює 90 днів

# Розрахунок прибутку для кожного виробника
factories = {
    "DeLonghi": DeLonghiFactory(),
    "Philips": PhilipsFactory(),
    "Jura": JuraFactory()
}

coffee_shop = CoffeeShop(coffee_prices, coffee_costs, daily_sales, days)

profit_results = {}

for manufacturer, factory in factories.items():
    machine = factory.create_machine()
    profit_results[manufacturer] = coffee_shop.calculate_profit(machine)

# Побудова таблиці з результатами
import pandas as pd

profit_df = pd.DataFrame(list(profit_results.items()), columns=["Manufacturer", "Profit"])
print(profit_df)

# Визначення найкращого виробника
best_manufacturer = max(profit_results, key=profit_results.get)
best_manufacturer
