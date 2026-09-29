"""Interactive calculator REPL with history and special commands."""

from app.calculation import CalculationFactory

MENU = """
Available commands:
  add <a> <b>       Add two numbers
  subtract <a> <b>  Subtract b from a
  multiply <a> <b>  Multiply two numbers
  divide <a> <b>    Divide a by b
  history           Show all calculations from this session
  help              Show this message
  exit              Quit the calculator
"""


def calculator():
    """Run a REPL that performs arithmetic and records a history."""
    history = []
    print("Welcome to the calculator REPL! Type 'help' for commands.")

    while True:
        user_input = input(">>> ").strip()

        if not user_input:
            continue

        command = user_input.lower()

        if command == "exit":
            print("Exiting calculator...")
            break

        if command == "help":
            print(MENU)
            continue

        if command == "history":
            if not history:
                print("No calculations yet.")
            else:
                for entry in history:
                    print(entry)
            continue

        try:
            operation, first, second = user_input.split()
            a, b = float(first), float(second)
        except ValueError:
            print("Invalid input. Format: <operation> <a> <b>. Type 'help' for commands.")
            continue

        try:
            calculation = CalculationFactory.create(operation.lower(), a, b)
            result = calculation.compute()
        except ValueError as error:
            print(error)
            continue

        history.append(calculation)
        print(f"Result: {result}")
