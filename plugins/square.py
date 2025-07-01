from calculator.plugin_base import PluginCommand

class SquareCommand(PluginCommand):
    def name(self):
        return "square"

    def execute(self, *args):
        x = args[0]
        return x * x

    def get_description(self):
        return "Squares a single number"
