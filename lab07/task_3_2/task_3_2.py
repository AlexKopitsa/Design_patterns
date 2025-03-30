class Vehicle:
    def __init__(self, age, model, damaged, mileage):
        self.age = age
        self.model = model
        self.damaged = damaged
        self.mileage = mileage

    def getAge(self): return self.age
    def getModel(self): return self.model
    def getDamage(self): return self.damaged
    def getMileage(self): return self.mileage

class VehicleCalculator:
    def setVehicle(self, vehicle): pass
    def calculatePrice(self): pass

class CarCalculator(VehicleCalculator):
    def __init__(self):
        self.vehicle = None

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def calculatePrice(self):
        base = 10_000
        reduction = self.vehicle.getAge() * 500 + self.vehicle.getDamage() * 2_000 + self.vehicle.getMileage() * 0.05
        return f"${max(base - reduction, 1000):.2f}"

class Auto:
    def __init__(self, age, model, damaged, mileage):
        self.age = age
        self.model = model
        self.damaged = damaged
        self.mileage = mileage

class Customs:
    def vehiclePrice(self, auto: Auto) -> float: pass
    def tax(self, auto: Auto) -> float: pass

class AdapterAutoToVehicle(Customs):
    def __init__(self):
        self.usd_to_uah = 39.0  # курс гривні

    def _to_vehicle(self, auto: Auto):
        return Vehicle(
            age=auto.age,
            model=auto.model,
            damaged=1.0 if auto.damaged else 0.0,
            mileage=auto.mileage
        )

    def vehiclePrice(self, auto: Auto) -> float:
        vehicle = self._to_vehicle(auto)
        calc = CarCalculator() if auto.model.lower() != "truck" else TruckCalculator()
        calc.setVehicle(vehicle)
        usd_price = float(calc.calculatePrice().replace("$", ""))
        return usd_price * self.usd_to_uah

    def tax(self, auto: Auto) -> float:
        return self.vehiclePrice(auto) * 0.2  # умовно 20% мито

if __name__ == "__main__":
    customs = AdapterAutoToVehicle()
    car = Auto(5, "Audi", False, 120_000)

    print("Ціна в гривнях:", customs.vehiclePrice(car))
    print("Мито в гривнях:", customs.tax(car))
