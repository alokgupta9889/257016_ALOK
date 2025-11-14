from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(vehicle):
        def start(self):
            print("car started")

class Bike(vehicle):
    def start(self):
        print("Bike started")
vehicles = [Car(), Bike()]
for v in vehicles:
     v.start()