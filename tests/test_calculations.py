"""Parameterized tests for the calculation classes and factory."""

import pytest

from app.calculation import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
    CalculationFactory,
)


@pytest.mark.parametrize("cls, a, b, expected", [
    (Addition, 2, 3, 5),
    (Subtraction, 5, 3, 2),
    (Multiplication, 4, 5, 20),
    (Division, 10, 2, 5),
])
def test_compute(cls, a, b, expected):
    """Each calculation class returns the correct result."""
    assert cls(a, b).compute() == expected


def test_operands_are_stored():
    """A calculation stores the operands it was created with."""
    calculation = Addition(2, 3)
    assert calculation.a == 2
    assert calculation.b == 3


@pytest.mark.parametrize("cls, a, b, expected", [
    (Addition, 2, 3, "2 + 3 = 5"),
    (Subtraction, 5, 3, "5 - 3 = 2"),
    (Multiplication, 4, 5, "4 * 5 = 20"),
    (Division, 10, 2, "10 / 2 = 5.0"),
])
def test_str(cls, a, b, expected):
    """Each calculation prints a readable record of itself."""
    assert str(cls(a, b)) == expected


def test_division_by_zero_raises():
    """Dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Division(1, 0).compute()


@pytest.mark.parametrize("operation, cls", [
    ("add", Addition),
    ("subtract", Subtraction),
    ("multiply", Multiplication),
    ("divide", Division),
])
def test_factory_creates_correct_type(operation, cls):
    """The factory returns the right class for each operation name."""
    assert isinstance(CalculationFactory.create(operation, 1, 2), cls)


def test_factory_rejects_unknown_operation():
    """The factory raises a ValueError for an unsupported operation."""
    with pytest.raises(ValueError, match="Unknown operation 'modulus'."):
        CalculationFactory.create("modulus", 1, 2)


def test_factory_lists_supported_operations():
    """The factory reports the operations it supports."""
    assert CalculationFactory.supported() == ["add", "subtract", "multiply", "divide"]
