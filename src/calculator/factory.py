import os
from .commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from .strategies import AdditionStrategy, SubtractionStrategy, MultiplicationStrategy, DivisionStrategy
from calculator.plugin_loader import load_plugins
from dotenv import load_dotenv

class CommandFactory:
    def __init__(self):
        load_dotenv()
        plugin_dir = os.getenv('PLUGIN_DIR', 'plugins')
        self.plugins = load_plugins(plugin_dir)

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
        elif command_name in self.plugins:
            return self.plugins[command_name]
        else:
            raise ValueError(f"Unknown command: {command_name}")
