class Transport:
    """Базовий клас для всіх видів транспорту."""
    def __init__(self, manufacturer, cost, usage_cost):
        self.manufacturer = manufacturer  # Виробник (Volvo, Skoda, Hyundai)
        self.cost = cost  # Вартість одиниці транспорту
        self.usage_cost = usage_cost  # Вартість експлуатації за 1 км

    def get_total_cost(self, distance, quantity):
        """Розрахунок загальної вартості для певного пробігу."""
        return quantity * (self.cost + self.usage_cost * distance)


class Bus(Transport):
    """Клас Автобус."""
    def go_by_way(self):
        """Відповідність методу з Java."""
        print("Bus runs!")


class Tram(Transport):
    """Клас Трамвай."""
    def go_by_rails(self):
        """Відповідність методу з Java."""
        print("Tram runs!")


class Trolleybus(Transport):
    """Клас Тролейбус."""
    def go_by_contact_network(self):
        """Відповідність методу з Java."""
        print("Trolleybus runs")


def calculate_best_manufacturer(A, T, Tr, N):
    """Функція визначає найкращого виробника транспорту з мінімальними витратами."""

    # Дані про вартість транспорту та експлуатації (з таблиць)
    manufacturers = {
        "Volvo": {
            "Bus": Bus("Volvo", 6_000_000, 20),
            "Tram": Tram("Volvo", 10_000_000, 7),
            "Trolleybus": Trolleybus("Volvo", 7_000_000, 13)
        },
        "Skoda": {
            "Bus": Bus("Skoda", 4_500_000, 25),
            "Tram": Tram("Skoda", 9_000_000, 8),
            "Trolleybus": Trolleybus("Skoda", 6_800_000, 12)
        },
        "Hyundai": {
            "Bus": Bus("Hyundai", 5_500_000, 20),
            "Tram": Tram("Hyundai", 9_500_000, 6),
            "Trolleybus": Trolleybus("Hyundai", 7_000_000, 11)
        }
    }

    # Збереження загальних витрат для кожного виробника
    total_costs = {}

    for manufacturer, transport in manufacturers.items():
        total_cost = 0
        total_cost += transport["Bus"].get_total_cost(N, A)
        total_cost += transport["Tram"].get_total_cost(N, T)
        total_cost += transport["Trolleybus"].get_total_cost(N, Tr)
        total_costs[manufacturer] = total_cost

    # Знаходження виробника з мінімальною вартістю контракту
    best_manufacturer = min(total_costs, key=total_costs.get)

    return best_manufacturer, total_costs


# Вхідні дані з умови
A = 10   # Кількість автобусів
T = 5    # Кількість трамваїв
Tr = 40  # Кількість тролейбусів
N = 200_000  # Орієнтовний пробіг транспорту

# Розрахунок найкращого виробника
best_manufacturer, total_costs = calculate_best_manufacturer(A, T, Tr, N)

# Відображення результатів у таблиці
import pandas as pd

cost_df = pd.DataFrame(list(total_costs.items()), columns=["Manufacturer", "Total Cost"])
print(cost_df)

# Вивід найкращого варіанту
best_manufacturer
