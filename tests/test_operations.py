"""Parameterized tests for the arithmetic operations."""

import pytest

from app.operation import addition, subtraction, multiplication, division


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_addition(a, b, expected):
    """Test addition across positive, negative, and zero values."""
    assert addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
])
def test_subtraction(a, b, expected):
    """Test subtraction with positive and negative results."""
    assert subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 15),
    (-3, -2, 6),
    (-4, 0, 0),
    (-2, 3, -6),
])
def test_multiplication(a, b, expected):
    """Test multiplication including negatives and zero."""
    assert multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-6, 2, -3),
    (0, 5, 0),
    (10, 3, 3.333333),
])
def test_division(a, b, expected):
    """Test division, using approx for non-terminating results."""
    assert division(a, b) == pytest.approx(expected)


def test_division_by_zero():
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)
