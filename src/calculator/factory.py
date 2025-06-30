from .commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from .strategies import AdditionStrategy, SubtractionStrategy, MultiplicationStrategy, DivisionStrategy

class CommandFactory:
    def get_command(self, command_name):
        command_name = command_name.lower()

        if command_name == "add":
            return AddCommand(AdditionStrategy())
        elif command_name == "subtract":
            return SubtractCommand(SubtractionStrategy())
        elif command_name == "multiply":
            return MultiplyCommand(MultiplicationStrategy())
        elif command_name == "divide":
            return DivideCommand(DivisionStrategy())
        else:
            raise ValueError(f"Unknown command: {command_name}")
