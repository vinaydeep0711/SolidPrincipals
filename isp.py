"""
Interface Segregation Principle-

Idea is very simple that you don't want to implement to many methods or functions into an interface
So define one interface and let the client implement however they want to implement

"""


"""Lets try to understand this with our LSP example"""

class Car:

    def on(self):
        pass

    def off(self):
        pass

    def auto_drive(self):
        raise NotImplementedError()

    def manual_drive(self):
        raise NotImplementedError()


class NewCar(Car):

    def on(self):
        return "Turn on car"

    def off(self):
        return "Turn off car"

    def auto_drive(self):
        return "runs on auto drive mode"

    def manual_drive(self):
        return "runs on manual mode also"


class OldCar1(Car):
    def on(self):
        return "Turn on car"

    def off(self):
        return "Turn off car"

    def auto_drive(self):
        pass #1 way

    def manual_drive(self):
        return "runs on manual mode also"


class OldCar2(Car):
    def on(self):
        return "Turn on car"

    def off(self):
        return "Turn off car"

    def auto_drive(self):
        """Not supported!"""
        raise NotImplementedError('Old car can not run in auto mode!')

    def manual_drive(self):
        return "runs on manual mode also"



"""Now in the above class OldCar1, OldCar2 problem is that when a client implements OldCar1 it does't know that it can not auto drive but cleint is able to seee that there is a auto drive function """
"""But if client will implement auto_drive1 or 2 it will either see nothing as response or the app will crash due to exception"""

from abc import abstractmethod
"""How to fix this ? - again we can implement manual_drive and auto_drive interface"""

class Car:
    @abstractmethod
    def on(self):
        pass
    @abstractmethod
    def off(self):
        pass


class NewCar1(Car):

    @abstractmethod
    def auto_drive(self):
       pass


class OldCar3(Car):
    @abstractmethod
    def manual_drive(self):
        pass


class MyNewcar(NewCar1, OldCar3):
    def on(self):
        return "Turn on car"

    def off(self):
        return "Turn off car"

    def auto_drive(self):
        return "runs on auto drive mode"

    def manual_drive(self):
        return "runs on manual mode also"


class MyOldCar(OldCar3):
    def on(self):
        return "Turn on car"

    def off(self):
        return "Turn off car"

    def manual_drive(self):
        return "runs on manual mode also"









