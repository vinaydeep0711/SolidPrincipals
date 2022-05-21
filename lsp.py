"""
Liskov Substitution Principle -
A sub-class must be substitutable for its super-class.
A derived class can assume the place of its super class and everything should work as it is
"""

"""Lets understand with an example"""

class Vehical:

    def on(self):
        pass

    def off(self):
        pass

    def autodrive(self):
        pass


class Car(Vehical):

    def on(self):
        return "Turn on car"

    def off(self):
        return "Turn off car"

    def autodrive(self):
        return  "runs on auto drive mode"


class MotorBike(Vehical):
    def on(self):
        return "Turn on bike"

    def off(self):
        return "Turn off bike"

    # def autodrive(self):
    #     return  "runs on auto drive mode"



"""In the above code MotoreBike does not have a feature called autodrive so MotorBike can not implement Vehical, so it violates Liskov Substitution principal"""
"""All subclass of vehical type should be able to inherit from vehical base class without any issue"""

"""Lets see how we can fix this so that it will follow LSP"""


class NewVehical:

    def on(self):
        pass

    def off(self):
        pass


class AutomaticVehical(NewVehical):
    def auto_drive(self):
        pass


class NewCar(AutomaticVehical):

    def on(self):
        return "Turn on car"

    def off(self):
        return "Turn off car"

    def auto_drive(self):
        return "runs on auto drive mode"


class NewMotorBike(Vehical):
    def on(self):
        return "Turn on bike"

    def off(self):
        return "Turn off bike"








