import calculator, pytest

def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"

def test_calculator_minus_small():
    a: int = 10
    b: int = 10
    expected: int = 0

    # Act
    actual: int = calculator.minus(a, b)

    # Assert
    assert expected == actual, "small number minus"

def test_calculator_multiply_small():
    a: int = 10
    b: float = 0.1
    expected: float = 1.0

    # Act
    actual: float = calculator.multiply(a, b)

    # Assert
    assert expected == actual, "small numbers multiply"

def test_calculator_divide_small():
    a: int = 10
    b: float = 0.1
    expected: float = 100

    # Act
    actual: float = calculator.divide(a, b)

    # Assert
    assert expected == actual, "small numbers divide"

def test_calculator_power_small():
    a: int = 2
    b: int = 4
    expected: int = 16

    # Act
    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "small number power"

def test_calculator_power_small02():
    a: int = 3
    b: int = 2
    expected: int = 9

    # Act
    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "small number power"

def test_calculator_sqrt():
    a: int = 25
    expected: int = 5

    # Act
    actual: int = calculator.sqrt(a)

    # Assert
    assert expected == actual, "sqrt"

def test_calculator_sqrt_error():
    a: int = -5

    # Act
    with pytest.raises(ValueError) as e:
        calculator.sqrt(a)

def test_calculator_factorial():

    a: int = 4
    expected: int = 24

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "factorial"

def test_calculator_factorial02():
    a: int = 5
    expected: int = 120

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "factorial"

def test_calculator_factorial_error():
    a: int = -3

    # Act
    try:
        calculator.factorial(a)

        # Assert
        assert False, "Should raise ValueError"

    except ValueError as e:
        assert True