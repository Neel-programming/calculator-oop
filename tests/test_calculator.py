"""Tests for the calculator REPL."""

import pytest

from app.calculator import calculator


def run_repl(monkeypatch, capsys, typed):
    """Run the REPL with a scripted user and return everything it printed."""
    notes = iter(typed + ["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(notes))
    calculator()
    return capsys.readouterr().out


@pytest.mark.parametrize("typed, expected", [
    ("add 2 3", "Result: 5.0"),
    ("subtract 5 3", "Result: 2.0"),
    ("multiply 4 5", "Result: 20.0"),
    ("divide 10 2", "Result: 5.0"),
    ("divide 5 0", "Division by zero is not allowed."),
    ("modulus 5 3", "Unknown operation 'modulus'."),
    ("add two three", "Invalid input."),
    ("add 1", "Invalid input."),
])
def test_repl_single_command(monkeypatch, capsys, typed, expected):
    """Each command produces the expected output."""
    assert expected in run_repl(monkeypatch, capsys, [typed])


def test_help_lists_commands(monkeypatch, capsys):
    """The help command prints the menu."""
    output = run_repl(monkeypatch, capsys, ["help"])
    assert "Available commands:" in output


def test_history_when_empty(monkeypatch, capsys):
    """History reports when nothing has been calculated."""
    output = run_repl(monkeypatch, capsys, ["history"])
    assert "No calculations yet." in output


def test_history_records_calculations(monkeypatch, capsys):
    """History lists calculations in the order they were performed."""
    output = run_repl(monkeypatch, capsys, ["add 2 3", "multiply 4 5", "history"])
    assert "2.0 + 3.0 = 5.0" in output
    assert "4.0 * 5.0 = 20.0" in output


def test_failed_calculation_not_in_history(monkeypatch, capsys):
    """A calculation that raises is not recorded in history."""
    output = run_repl(monkeypatch, capsys, ["divide 5 0", "history"])
    assert "No calculations yet." in output


def test_blank_input_is_ignored(monkeypatch, capsys):
    """Pressing enter with no input re-prompts without an error."""
    output = run_repl(monkeypatch, capsys, ["", "add 1 1"])
    assert "Result: 2.0" in output
    assert "Invalid input." not in output


def test_exit_message(monkeypatch, capsys):
    """Exiting prints a goodbye message."""
    assert "Exiting calculator..." in run_repl(monkeypatch, capsys, [])
