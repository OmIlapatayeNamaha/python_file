from abc import *

class Car(ABC):
    def show(self):
        print("every car has four wheels")
    @abstractmethod
    def speed(self):
        pass
    
class Maruti(Car):
    def speed(self):
        print("speed is 100 km/hr ")
class thar(Car):
    def speed(self):
        print("speed is 70 km/hr ")
class BMW(Car):
    def speed(self):
        print("speed is 120 km/pr ")
obj1=Maruti()
obj1.show()
obj1.speed()
obj2=thar()
obj2.show()
obj2.speed()
obj3=BMW()
obj3.show()
obj3.speed()

                
