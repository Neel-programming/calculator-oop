"""Calculation classes and the factory that creates them."""

from abc import ABC, abstractmethod

from app.operation import addition, subtraction, multiplication, division


class Calculation(ABC):
    """Abstract base class for a single calculation."""

    def __init__(self, a: float, b: float):
        """Store the two operands."""
        self.a = a
        self.b = b

    @abstractmethod
    def compute(self) -> float:
        """Return the result of the calculation."""

    def __str__(self) -> str:
        """Return a readable record of the calculation."""
        return f"{self.a} {self.symbol} {self.b} = {self.compute()}"


class Addition(Calculation):
    """Addition of two numbers."""

    symbol = "+"

    def compute(self) -> float:
        """Return a plus b."""
        return addition(self.a, self.b)


class Subtraction(Calculation):
    """Subtraction of two numbers."""

    symbol = "-"

    def compute(self) -> float:
        """Return a minus b."""
        return subtraction(self.a, self.b)


class Multiplication(Calculation):
    """Multiplication of two numbers."""

    symbol = "*"

    def compute(self) -> float:
        """Return a times b."""
        return multiplication(self.a, self.b)


class Division(Calculation):
    """Division of two numbers."""

    symbol = "/"

    def compute(self) -> float:
        """Return a divided by b."""
        return division(self.a, self.b)


class CalculationFactory:
    """Create Calculation objects from an operation name."""

    _calculations = {
        "add": Addition,
        "subtract": Subtraction,
        "multiply": Multiplication,
        "divide": Division,
    }

    @classmethod
    def create(cls, operation: str, a: float, b: float) -> Calculation:
        """Return a Calculation for the given operation name."""
        if operation not in cls._calculations:
            raise ValueError(f"Unknown operation '{operation}'.")
        return cls._calculations[operation](a, b)

    @classmethod
    def supported(cls) -> list:
        """Return the list of supported operation names."""
        return list(cls._calculations)
