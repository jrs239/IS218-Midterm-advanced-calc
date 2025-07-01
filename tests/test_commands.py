import pytest
from calculator.commands import (
    AddCommand,
    SubtractCommand,
    MultiplyCommand,
    DivideCommand
)
from calculator.strategies import (
    AdditionStrategy,
    SubtractionStrategy,
    MultiplicationStrategy,
    DivisionStrategy
)

def test_add_command():
    strategy = AdditionStrategy()
    command = AddCommand(strategy)
    result = command.execute(2, 3)
    assert result == 5

def test_subtract_command():
    strategy = SubtractionStrategy()
    command = SubtractCommand(strategy)
    result = command.execute(10, 4)
    assert result == 6

def test_multiply_command():
    strategy = MultiplicationStrategy()
    command = MultiplyCommand(strategy)
    result = command.execute(6, 7)
    assert result == 42

def test_divide_command():
    strategy = DivisionStrategy()
    command = DivideCommand(strategy)
    result = command.execute(20, 4)
    assert result == 5

def test_divide_by_zero():
    strategy = DivisionStrategy()
    command = DivideCommand(strategy)
    with pytest.raises(ZeroDivisionError):
        command.execute(10, 0)

