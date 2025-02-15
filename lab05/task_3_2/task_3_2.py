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

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Wheel(material={self.material.value}, diameter={self.diameter})"


class Engine:
    def __init__(self, power: int, torque: int, fuel: Fuel, volume: float):
        self.power = power
        self.torque = torque
        self.fuel = fuel
        self.volume = volume

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Engine(power={self.power}, torque={self.torque}, fuel={self.fuel.value}, volume={self.volume})"


class Car:
    def __init__(self, car_type: CarType, car_color: CarColor, engine: Engine, wheel: Wheel):
        self.car_type = car_type
        self.car_color = car_color
        self.engine = engine
        self.wheel = wheel

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Car:\n  type={self.car_type.value},\n  color={self.car_color.value},\n  engine={self.engine},\n  wheel={self.wheel}"


# Тестування клонування
if __name__ == "__main__":
    original_car = Car(CarType.SEDAN, CarColor.BLACK, Engine(150, 200, Fuel.PETROL, 2.0), Wheel(Material.ALLOY, 16))
    cloned_car = original_car.clone()

    print("Оригінал:", original_car)
    print("Клон:", cloned_car)
