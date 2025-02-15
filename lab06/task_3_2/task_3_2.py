import copy
from enum import Enum

class Material(Enum):
    STEEL = "Steel"
    ALLOY = "Alloy"
    FORGED = "Forged"

class Fuel(Enum):
    PETROL = "Petrol"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"

class CarColor(Enum):
    WHITE = "White"
    BLACK = "Black"
    RED = "Red"
    GREY = "Grey"

class CarType(Enum):
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    SUV = "SUV"

class Wheel:
    def __init__(self, material: Material, diameter: int):
        self.material = material
        self.diameter = diameter

    def __str__(self):
        return f"Wheel(material={self.material.value}, diameter={self.diameter})"

class Engine:
    def __init__(self, power: int, torque: int, fuel: Fuel, volume: float):
        self.power = power
        self.torque = torque
        self.fuel = fuel
        self.volume = volume

    def __str__(self):
        return f"Engine(power={self.power}, torque={self.torque}, fuel={self.fuel.value}, volume={self.volume})"

class Car:
    def __init__(self, car_type: CarType, car_color: CarColor, engine: Engine, wheel: Wheel):
        self.car_type = car_type
        self.car_color = car_color
        self.engine = engine
        self.wheel = wheel

    def __str__(self):
        return f"Car:\n  type={self.car_type.value},\n  color={self.car_color.value},\n  engine={self.engine},\n  wheel={self.wheel}"

# Реалізація шаблону "Будівельник"
class CarBuilder:
    """Будівельник для поступового створення автомобіля."""
    def __init__(self):
        self.car_type = None
        self.car_color = None
        self.engine = None
        self.wheel = None

    def set_car_type(self, car_type: CarType):
        self.car_type = car_type
        return self

    def set_car_color(self, car_color: CarColor):
        self.car_color = car_color
        return self

    def set_engine(self, power: int, torque: int, fuel: Fuel, volume: float):
        self.engine = Engine(power, torque, fuel, volume)
        return self

    def set_wheel(self, material: Material, diameter: int):
        self.wheel = Wheel(material, diameter)
        return self

    def build(self):
        if None in [self.car_type, self.car_color, self.engine, self.wheel]:
            raise ValueError("Недостатньо параметрів для створення автомобіля")
        return Car(self.car_type, self.car_color, self.engine, self.wheel)

class Director:
    """Клас Директор, що визначає порядок побудови різних типів автомобілів."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Director, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def construct_sedan():
        return CarBuilder() \
            .set_car_type(CarType.SEDAN) \
            .set_car_color(CarColor.BLACK) \
            .set_engine(150, 200, Fuel.PETROL, 2.0) \
            .set_wheel(Material.ALLOY, 16) \
            .build()

    @staticmethod
    def construct_suv():
        return CarBuilder() \
            .set_car_type(CarType.SUV) \
            .set_car_color(CarColor.GREY) \
            .set_engine(200, 300, Fuel.DIESEL, 3.0) \
            .set_wheel(Material.FORGED, 18) \
            .build()

    @staticmethod
    def construct_hatchback():
        return CarBuilder() \
            .set_car_type(CarType.HATCHBACK) \
            .set_car_color(CarColor.RED) \
            .set_engine(120, 160, Fuel.PETROL, 1.6) \
            .set_wheel(Material.STEEL, 15) \
            .build()


# Тестування Одинака
if __name__ == "__main__":
    director1 = Director()
    director2 = Director()

    print("director1 is director2:", director1 is director2)  # Перевірка, що це один екземпляр

    sedan = director1.construct_sedan()
    suv = director1.construct_suv()
    hatchback = director1.construct_hatchback()

    print(sedan)
    print(suv)
    print(hatchback)
