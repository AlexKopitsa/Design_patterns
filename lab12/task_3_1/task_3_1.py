# === Flyweight ===
class Wheel:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Wheel[{self.type}]"

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def __str__(self):
        return f"Engine[{self.horsepower}HP]"


# === Flyweight Factory ===
class PartFactory:
    _wheels = {}
    _engines = {}

    @classmethod
    def get_wheel(cls, type):
        if type not in cls._wheels:
            cls._wheels[type] = Wheel(type)
        return cls._wheels[type]

    @classmethod
    def get_engine(cls, horsepower):
        if horsepower not in cls._engines:
            cls._engines[horsepower] = Engine(horsepower)
        return cls._engines[horsepower]


# === Car ===
class Car:
    def __init__(self, wheel, engine):
        self.wheel = wheel
        self.engine = engine

    def show_parts(self):
        print(f"Car parts: {self.wheel}, {self.engine}")


# === Car Builder ===
class CarBuilder:
    def build_car(self, wheel_type, engine_hp):
        wheel = PartFactory.get_wheel(wheel_type)
        engine = PartFactory.get_engine(engine_hp)
        return Car(wheel, engine)


# === Car Simulator ===
class CarSimulator:
    def __init__(self):
        self.cars = []
        self.builder = CarBuilder()

    def simulate(self):
        self.cars.append(self.builder.build_car("Sport", 300))
        self.cars.append(self.builder.build_car("Sport", 300))
        self.cars.append(self.builder.build_car("Offroad", 250))

        for car in self.cars:
            car.show_parts()


# === Тест ===
if __name__ == "__main__":
    sim = CarSimulator()
    sim.simulate()
