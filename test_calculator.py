from calculator import Calculator, CalculatorError
import pytest



def test_add():
    calculator = Calculator()
    result = calculator.add("helo", "helo")
    assert "helohelo" == result


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
    with pytest.raises(CalculatorError) as context:
        result = calculator.add("hello",2)
    
    assert str(context.value) == 'this does not accept a sring value'

def test_do_some_weirder_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("a","b")