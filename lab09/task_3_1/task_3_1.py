from abc import ABC, abstractmethod

# === Інтерфейс (компонент) ===
class ExpenseEntity(ABC):
    @abstractmethod
    def pay_expenses(self):
        pass

# === Manager (листок) ===
class Manager(ExpenseEntity):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def pay_expenses(self):
        print(f"{self.name} has been paid ${self.salary}")

# === Salesperson (листок) ===
class Salesperson(ExpenseEntity):
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager

    def pay_expenses(self):
        print(f"{self.name} has been paid ${self.salary}")

# === SalesTeam (композит) ===
class SalesTeam(ExpenseEntity):
    def __init__(self):
        self.entities = []  # список всіх ExpenseEntity

    def add(self, entity: ExpenseEntity):
        self.entities.append(entity)

    def pay_expenses(self):
        for entity in self.entities:
            entity.pay_expenses()

# === Client ===
def pay_entity(entity: ExpenseEntity):
    print("Expenses have been requested")
    entity.pay_expenses()
    print("Expenses have been paid\n")

# === Тестування ===
if __name__ == "__main__":
    jane = Manager("Jane", 100)
    bob = Salesperson("Bob", 300, jane)
    sue = Salesperson("Sue", 200, jane)

    team = SalesTeam()
    team.add(jane)
    team.add(bob)
    team.add(sue)

    pay_entity(jane)
    pay_entity(bob)
    pay_entity(team)