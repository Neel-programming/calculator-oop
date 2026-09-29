"""Arithmetic operations for the calculator."""


def addition(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtraction(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiplication(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def division(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
