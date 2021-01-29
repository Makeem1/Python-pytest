from calculator import Calculator, CalculatorError
import pytest



def test_add():
    calculator = Calculator()
    result = calculator.add(5, 7)
    assert 12 == result


def test_substract():
    calculator = Calculator()
    result = calculator.subtract(7,2)
    assert 5 == result


def test_divide():
    calculator = Calculator()
    result = calculator.divide(10,2)
    assert 5 == result

def test_subtract():
    calculator = Calculator()
    result = calculator.multiply(2,4)
    assert 8 == result

def test_wierd_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("two", "3")



def test_wierder_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add('hello', 'wolrd')


def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)
    

