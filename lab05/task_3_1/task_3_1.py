import numpy as np
import copy


class Equation:
    """Базовий клас рівнянь з підтримкою прототипу."""

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def solve(self):
        raise NotImplementedError("Метод solve() має бути реалізований у підкласах.")

    def clone(self):
        """Створює клон об'єкта рівняння."""
        return copy.deepcopy(self)


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
            return LinearEquation([b, c]).solve()
        D = b ** 2 - 4 * a * c
        if D < 0:
            return []
        elif D == 0:
            return [-b / (2 * a)]
        else:
            sqrt_D = np.sqrt(D)
            return [(-b + sqrt_D) / (2 * a), (-b - sqrt_D) / (2 * a)]


class BiQuadraticEquation(Equation):
    """Клас для бі-квадратного рівняння ax^4 + bx^2 + c = 0."""

    def solve(self):
        if len(self.coefficients) != 5:
            return None
        a, _, b, _, c = self.coefficients
        if a == 0:
            return QuadraticEquation([b, c, 0]).solve()
        quadratic_solutions = QuadraticEquation([a, b, c]).solve()
        solutions = []
        for y in quadratic_solutions:
            if y < 0:
                continue
            solutions.append(np.sqrt(y))
            solutions.append(-np.sqrt(y))
        return solutions


# Тестування клонування
if __name__ == "__main__":
    eq1 = QuadraticEquation([1, -3, 2])  # x^2 - 3x + 2 = 0
    eq2 = eq1.clone()  # Клонування

    print("Оригінал:", eq1.solve())
    print("Клон:", eq2.solve())
