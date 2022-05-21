"""
Single Responsibility Principal -
A class should have only one responsibility, if one class is assigned multiple responsibility it leads to multiple modifications
in the future and classed will be coupled with other classes due to that if one functionality breaks it will lead to failure.
"""

class Car:

    def __init__(self, name:str):
        self.name = name

    def drive(self):
        return "Hey I am car! I can run"

    def cook_food(self):
        return "Trying to cook food! while driving"


"""Above class violates the responsibility of SRP you can see a Car class has been given two responsibility drive and cook food"""
"""A cars responsibility is to drive only not to cook the food  this violates SRP principal"""

"""How to fix ? - We will create another class which will handle the responsibility of cooking and driving separately"""


class NewCar:

     def drive(self):
         return "Hey I am car! I can run"

     
class Cook:

    def cook_food(self):
        return "I am cook I can cook food happily"












