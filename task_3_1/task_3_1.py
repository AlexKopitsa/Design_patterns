class Wheel:
    def __init__(self):
        print("Wheel created")

class Engine:
    def __init__(self):
        print("Engine created")

class Car:
    def __init__(self):
        self.wheels = [Wheel() for _ in range(4)]  # Машина має 4 колеса
        self.engine = Engine()
        print("Car created")

class CarBuilder:
    def build_car(self):
        return Car()

class CarSimulator:
    def __init__(self):
        self.car_builder = CarBuilder()

    def simulate(self):
        print("Simulating car...")
        car = self.car_builder.build_car()
        print("Simulation complete")

if __name__ == "__main__":
    simulator = CarSimulator()
    simulator.simulate()
