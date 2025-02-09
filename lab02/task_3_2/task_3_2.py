import numpy as np
import pandas as pd

class Equation:
    """Базовий клас рівнянь."""
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def solve(self):
        """Метод для розв’язку рівняння."""
        raise NotImplementedError("Метод solve() має бути реалізований у підкласах.")

class LinearEquation(Equation):
    """Клас для лінійного рівняння bx + c = 0."""
    def solve(self):
        if len(self.coefficients) != 2:
            return None
        b, c = self.coefficients
        if b == 0:
            return [] if c != 0 else ["∞"]  # Нескінченна кількість розв'язків
        return [-c / b]

class QuadraticEquation(Equation):
    """Клас для квадратного рівняння ax^2 + bx + c = 0."""
    def solve(self):
        if len(self.coefficients) != 3:
            return None
        a, b, c = self.coefficients
        if a == 0:
            return LinearEquation([b, c]).solve()  # Перетворюємо у лінійне рівняння

        D = b**2 - 4*a*c  # Дискримінант
        if D < 0:
            return []  # Немає коренів
        elif D == 0:
            return [-b / (2 * a)]  # Один корінь
        else:
            sqrt_D = np.sqrt(D)
            return [(-b + sqrt_D) / (2 * a), (-b - sqrt_D) / (2 * a)]

class BiQuadraticEquation(Equation):
    """Клас для бі-квадратного рівняння ax^4 + bx^2 + c = 0."""
    def solve(self):
        if len(self.coefficients) != 5:
            return None
        a, _, b, _, c = self.coefficients  # Пропускаємо нульові коефіцієнти
        if a == 0:
            return QuadraticEquation([b, c, 0]).solve()

        quadratic_solutions = QuadraticEquation([a, b, c]).solve()
        solutions = []
        for y in quadratic_solutions:
            if y < 0:
                continue  # Відкидаємо від'ємні значення
            solutions.append(np.sqrt(y))
            solutions.append(-np.sqrt(y))
        return solutions

def parse_equation(line):
    """Парсить рядок у список коефіцієнтів та визначає тип рівняння."""
    coeffs = list(map(int, line.split()))
    if len(coeffs) == 2:
        return LinearEquation(coeffs)
    elif len(coeffs) == 3:
        return QuadraticEquation(coeffs)
    elif len(coeffs) == 5:
        return BiQuadraticEquation(coeffs)
    else:
        return None

def process_file(filename):
    """Обробка файлу та класифікація рівнянь."""
    results = {
        "no_solutions": [],
        "one_solution": [],
        "two_solutions": [],
        "three_solutions": [],
        "four_solutions": [],
        "infinite_solutions": []
    }
    all_solutions = []

    with open(filename, "r") as file:
        for line in file:
            equation = parse_equation(line)
            if equation:
                solutions = equation.solve()
                if solutions is None:
                    continue

                num_solutions = len(solutions) if "∞" not in solutions else float("inf")
                all_solutions.append((line.strip(), num_solutions))

                if solutions == []:
                    results["no_solutions"].append(line.strip())
                elif num_solutions == 1:
                    results["one_solution"].append(line.strip())
                elif num_solutions == 2:
                    results["two_solutions"].append(line.strip())
                elif num_solutions == 3:
                    results["three_solutions"].append(line.strip())
                elif num_solutions == 4:
                    results["four_solutions"].append(line.strip())
                elif num_solutions == float("inf"):
                    results["infinite_solutions"].append(line.strip())

    # Знаходимо рівняння з найбільшою та найменшою кількістю розв’язків
    min_eq = min(all_solutions, key=lambda x: x[1], default=None)
    max_eq = max(all_solutions, key=lambda x: x[1], default=None)

    # Середнє значення кількості розв’язків для рівнянь, що мають хоча б один розв’язок
    valid_solutions = [eq[1] for eq in all_solutions if eq[1] > 0]
    avg_solutions = sum(valid_solutions) / len(valid_solutions) if valid_solutions else None

    return results, min_eq, max_eq, avg_solutions

# Обробка всіх файлів
files = ["input01.txt", "input02.txt", "input03.txt"]
results_summary = {}

for file in files:
    results, min_eq, max_eq, avg_solutions = process_file(file)
    results_summary[file] = {
        "results": results,
        "min_eq": min_eq,
        "max_eq": max_eq,
        "avg_solutions": avg_solutions
    }

# Створення таблиці для аналізу категорій рівнянь
output_df = pd.DataFrame(columns=["Filename", "Category", "Equations"])

for filename, data in results_summary.items():
    for category, equations in data["results"].items():
        output_df = pd.concat([output_df, pd.DataFrame([{"Filename": filename, "Category": category, "Equations": len(equations)}])], ignore_index=True)

print(output_df)

# Створення таблиці для мінімального, максимального та середнього значення розв’язків
detailed_results = []

for filename, data in results_summary.items():
    min_eq = data["min_eq"]
    max_eq = data["max_eq"]
    avg_solutions = data["avg_solutions"]

    detailed_results.append({
        "Filename": filename,
        "Category": "Equation with min solutions",
        "Equation": min_eq[0] if min_eq else "N/A",
        "Solutions": min_eq[1] if min_eq else "N/A"
    })

    detailed_results.append({
        "Filename": filename,
        "Category": "Equation with max solutions",
        "Equation": max_eq[0] if max_eq else "N/A",
        "Solutions": max_eq[1] if max_eq else "N/A"
    })

    detailed_results.append({
        "Filename": filename,
        "Category": "Average solutions count",
        "Equation": "N/A",
        "Solutions": avg_solutions if avg_solutions else "N/A"
    })

# Відображення таблиці з детальним аналізом
detailed_df = pd.DataFrame(detailed_results)
print(detailed_df)