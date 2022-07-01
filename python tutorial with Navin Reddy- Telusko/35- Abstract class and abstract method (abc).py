# Prevents a user from creating an object of that class
# compels an user to override abstract methods in a child class. This
# abstract class: a class which contains one or more abstract methods
#abstract method: a method that has a declaration but does not have an implementation
# when you apply abstract method to a child class it doesn't work if you forget a method/function which in parent class
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class car(vehicle):
    def go(self):
        print("you drive the car")
        
 
    def stop(self):
        print("car is stopped")
class motorcycle(vehicle):
    #pass  # if you add pass python won't allow you to run the program wihtout method/s in parent class
    def go(self):
        print("you drive the motorcycle")
 
    def stop(self):
        print("motorcycle is stopped")

#v1=vehicle()
car1=car()
car1.go()
car1.stop()
mc1=motorcycle()
mc1.go()
mc1.stop()
