"""
Dependency Inversion Principal -

High level module/class should not directly depend upon low level class instead they should depend on abstractions
There should not be a tight coupling between classes.

The dependency inversion principle aims to reduce the coupling between classes by creating an abstraction layer between them

"""


class FXConverter:

    def convert(self, from_curr, to_curr, amount):
        print(f'{amount}{from_curr}={amount}{to_curr}')
        return amount*1.2

class App:
    def start(self):
        converter = FXConverter()   #dependency on FXConverter class
        converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App()
    app.start()




"Fix using an interface class"

from abc import abstractmethod, ABC


class ICurrencyConverter(ABC):
    @abstractmethod
    def convert(self, from_currency, to_currency, amount):
        pass


class FXConverter(ICurrencyConverter):

    def convert(self, from_curr, to_curr, amount):
        print(f'{amount}{from_curr}={amount}{to_curr}')
        return amount*1.2


class AlphaConverter(ICurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15


class App:
    def __init__(self, converter: ICurrencyConverter):
        self.converter = converter  #depends on Interface than the class

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__=='__main__':
    converter1 = AlphaConverter()
    app = App(converter1)
    app.start()

    converter2 = FXConverter()
    app = App(converter2)
    app.start()





