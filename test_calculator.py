from calculator import Calculator, CalculatorError
import pytest



def test_add():
    calculator = Calculator()
    result = calculator.add(5,7)
    assert 12==result


def test_substract():
    calculator = Calculator()
    result = calculator.subtract(7,2)
    assert 5 == result


def test_divide():
    calculator = Calculator()
    result = calculator.divide(10,2)
    assert 5 == result

def test_do_some_weird_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.subtract('add',2)
    assert 5 == result