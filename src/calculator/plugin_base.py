from abc import ABC, abstractmethod

class PluginCommand(ABC):
    @abstractmethod
    def name(self):
        """Name of the command (user types this)"""
        pass

    @abstractmethod
    def execute(self, *args):
        """Perform the operation"""
        pass

    @abstractmethod
    def get_description(self):
        """Description for help text"""
        pass
