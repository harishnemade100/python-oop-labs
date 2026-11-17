# ---------- Step 1: the parts ----------
class Engine:
    def start(self):
        print("petrol engine starts")

class Transmission:
    def shift(self):
        print("gear shifts")

class GPS:
    def navigate(self):
        print("navigating")


# ---------- Step 2: Car INHERITS its parts (the wrong "is-a") ----------
class Car(Engine, Transmission, GPS):
    pass


# ---------- Step 3: ElectricCar ----------
class ElectricCar(Car):
    pass


# ---------- Step 4: HybridCar ----------
# Needs petrol engine AND electric motor. Inheritance forces a workaround.
class ElectricMotor:
    def start(self):
        print("electric motor starts")

class HybridCar(Car, ElectricMotor):
    pass


# ---------- Run and observe ----------
if __name__ == "__main__":
    print("--- Car ---")
    car = Car()
    car.start()
    car.shift()
    car.navigate()

    print("--- ElectricCar ---")
    ev = ElectricCar()
    ev.start()      # PROBLEM 1: prints "petrol engine starts"
    ev.shift()      # PROBLEM 2: an EV usually has no gears

    print("--- HybridCar ---")
    hybrid = HybridCar()
    hybrid.start()  # PROBLEM 3: which start runs? Only one wins
    print(HybridCar.__mro__)