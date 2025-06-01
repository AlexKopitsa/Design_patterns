from abc import ABC, abstractmethod

# === Mediator ===
class Dispatcher:
    def __init__(self):
        self.planes_in_flight = []
        self.planes_on_ground = []
        self.runway_free = True

    def register_flight(self, plane):
        self.planes_in_flight.append(plane)

    def register_ground(self, plane):
        self.planes_on_ground.append(plane)

    def request_takeoff(self, plane):
        if self.runway_free:
            print(f"{plane.name} is taking off.")
            self.runway_free = False
            self.planes_on_ground.remove(plane)
            self.planes_in_flight.append(plane)
        else:
            print(f"{plane.name} is waiting to take off. Runway is busy.")

    def request_landing(self, plane):
        if self.runway_free:
            print(f"{plane.name} is landing.")
            self.runway_free = False
            self.planes_in_flight.remove(plane)
            self.planes_on_ground.append(plane)
        else:
            print(f"{plane.name} is waiting to land. Runway is busy.")

    def free_runway(self):
        self.runway_free = True
        print("Runway is now free.")


# === Colleague ===
class Plane:
    def __init__(self, name, mediator: Dispatcher):
        self.name = name
        self.mediator = mediator

    def take_off(self):
        self.mediator.request_takeoff(self)

    def land(self):
        self.mediator.request_landing(self)

    def runway_cleared(self):
        self.mediator.free_runway()


# === Client ===
if __name__ == "__main__":
    tower = Dispatcher()

    p1 = Plane("Flight A1", tower)
    p2 = Plane("Flight B2", tower)
    p3 = Plane("Flight C3", tower)

    tower.register_ground(p1)
    tower.register_ground(p2)
    tower.register_flight(p3)

    p1.take_off()      # Should take off
    p2.take_off()      # Should wait
    p1.runway_cleared()
    p2.take_off()      # Now should take off

    p3.land()          # Should wait
    p2.runway_cleared()
    p3.land()          # Now should land
