from abc import ABC, abstractmethod

# Інтерфейс продукту
class Product(ABC):
    @abstractmethod
    def do_something(self):
        pass

# Конкретні продукти
class Product1(Product):
    def do_something(self):
        return "Product1: Виконано дію"

class Product2(Product):
    def do_something(self):
        return "Product2: Виконано дію"

# Абстрактний клас творця
class Creator(ABC):
    @abstractmethod
    def create_product(self) -> Product:
        pass

    def some_operation(self):
        product = self.create_product()
        return product.do_something()

# Конкретні творці
class ConcreteCreator1(Creator):
    def create_product(self) -> Product:
        return Product1()

class ConcreteCreator2(Creator):
    def create_product(self) -> Product:
        return Product2()


if __name__ == "__main__":
    creator1 = ConcreteCreator1()
    print(creator1.some_operation())

    creator2 = ConcreteCreator2()
    print(creator2.some_operation())
