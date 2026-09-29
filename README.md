# Calculator REPL (OOP)

A command-line calculator built in Python using object-oriented design. Calculations are modeled as classes created by a factory, and each session keeps a history of what was computed. Tested with pytest at 100% coverage, enforced by GitHub Actions.

## Features

- Addition, subtraction, multiplication, and division
- REPL interface with continuous user interaction
- Special commands: `help`, `history`, `exit`
- Session history of all successful calculations
- Input validation and graceful error handling
- Both LBYL and EAFP error-handling paradigms

## Design

Each calculation is an object rather than a bare function call, so it can remember its own operands and describe itself.

- `Calculation` is an abstract base class holding the operands and the string representation.
- `Addition`, `Subtraction`, `Multiplication`, and `Division` inherit from it and define only their own math.
- `CalculationFactory` creates the right subclass from the operation the user typed, so the REPL never needs to know which classes exist.

### Error handling paradigms

**LBYL (Look Before You Leap)** is used where a condition can be checked cheaply up front: the factory verifies an operation exists before creating a calculation, and the REPL checks for empty input before parsing it.

**EAFP (Easier to Ask Forgiveness than Permission)** is used where checking in advance would duplicate the work: the REPL attempts to split and convert the input, then handles a `ValueError` if the format was wrong.

## Project Structure

```
calculator-oop/
    app/
        calculator/__init__.py   REPL loop, commands, history
        calculation/__init__.py  Calculation classes and factory
        operation/__init__.py    Arithmetic functions
    tests/
        test_calculator.py       REPL tests
        test_calculations.py     Class and factory tests
        test_operations.py       Arithmetic tests
    .github/workflows/
        python-app.yml           CI: tests and 100% coverage gate
    main.py
