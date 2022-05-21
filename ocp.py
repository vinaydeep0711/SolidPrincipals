"""
Open Closed Principal -
Classes, functions or modules should be open for extension and not for modifications
"""
class Car:

    def get_name(self):
        pass

    def car_speed(self, cars):
        for car in cars:
            if car=="TATA":
                yield "100 km/hour"
            elif car=="Honda":
                yield "200 km/hour"
            elif car=="BMW":
                yield "300 km/hour"


car = Car()
car.car_speed("TATA")
car.car_speed("Honda")
car.car_speed(("BMW"))


"""The function car_speed does not confirm Open closed principal because if we have tp add new car type we have to modify car_speeed method"""

"""This is quite a simple example. When your application grows and becomes complex, 
you will see that the if statement would be repeated over and over again 
in the car_speed function each time a new car type is added, all over the application"""


"""How can we fix this to follow OCP principal"""

from abc import abstractmethod

class ICar:

    @abstractmethod
    def car_speed(self, cars):
       pass


class TATA(ICar):

    def car_speed(self, cars):
        return "100 km/hour"


class Honda(ICar):

    def car_speed(self, cars):
        return "200 km/hour"


class BMW(ICar):

    def car_speed(self, cars):
        return "600 km/hour"


"""So in the above we have now made Car as abstract class ICar which has abstract method car_speed now all the car type will implement car_speed in their own way """
"""If we need to add new car type we don't have to modify car_speed in Car class, car_speed now conforms to the OCP principle"""






