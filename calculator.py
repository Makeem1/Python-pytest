class CalculatorError(Exception):
    """An exception for calculator"""

class Calculator():
    """Calculator for trying how pytest works"""

    def add(self, a , b):
        try:
            return a + b
        except TypeError:
            raise CalculatorError('this does not accept a sring value')


    def subtract(self, a, b ):
        return a - b

    def divide(self, a, b ):
        return a / b

    # def do_weird_stuff(self, a , b):
    #     return 

         