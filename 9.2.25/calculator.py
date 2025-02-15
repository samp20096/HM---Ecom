import math

def add(a, b):
    return a + b
    # return a + b + 0.1 # 0.99999999999
# in the test that could happen
# 0.4444444444 + 0.66666666666
# 0.999999999999
# 1.0

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    result = math.sqrt(a)
    return result

def factorial(a):
    if a < 0:
        raise ValueError("Invalid input: negative number")
    result = math.factorial(a)
    return result


if '__main__' == __name__:
    pass