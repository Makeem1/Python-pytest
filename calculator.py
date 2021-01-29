import numbers
import sys

class CalculatorError(Exception):
    """An exception for calculator"""

class Calculator():
    """Calculator for trying how pytest works"""

    def add(self, a , b):
        self._check_operand(a)
        self._check_operand(b)
        return a + b 


    def subtract(self, a, b ):
        return a - b

    def multiply(self, a, b ):
        return a * b

    def divide(self, a, b ):
        try:
            return a / b
        except ZeroDivisionError as es:
            raise CalculatorError("Can't divide by Zero")

    def _check_operand(self, operand):
        """Check that the operand is a number."""
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number.')
         

if __name__ == "__main__":
    print("Pick an operation to perform")
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.divide,
        calculator.multiply
    ]

    while True:
        for index, operation in enumerate(operations, start=1):
            print(f"'{index}' ----- {operation.__name__}")
        
        operation = input("Select an operation to perform a task: ")
            
        if operation == "q":
            sys.exit()
        op = int(operation)
        a = float(input("what is a "))
        b = float(input("what is b "))

        try:
            print(operations[op - 1](a,b))
        except CalculatorError as ex:
            print('can\'t divide by zero')