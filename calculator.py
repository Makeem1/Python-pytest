import numbers
import sys

class CalculatorError(Exception):
    """An exception for calculator"""

class MyError(Exception):
    """An exception error for a particular parameter"""

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
            return a/b 
        except ZeroDivisionError as es:
            raise CalculatorError("Can't divide by zero") from es
        

    def _check_operand(self, operand):
        """Check that the operand is a number."""
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number.')

    def add_int(self, a , b):
        if a == 99:
            raise MyError()
        else:
            return a + b 
            
         

if __name__ == "__main__":
    print("Pick an operation to perform")
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.divide,
        calculator.multiply
    ]

    operation_num = [
        1,
        2,
        3,
        4
    ]

    while True:
        print("Pick an operation to perform : ")
        for index, operation in enumerate(operations, start=1):
            print(f"'{index}' ----- {operation.__name__}")
        
        operation = input("Select an operation to perform a task: ")
            
        if operation == "q":
            sys.exit()
        if int(operation) not in operation_num:
            sys.exit()

        op = int(operation)
        a = float(input("what is a "))
        b = float(input("what is b "))

        try:
            print(operations[op - 1](a,b))
        except CalculatorError as ex:
            print(es)