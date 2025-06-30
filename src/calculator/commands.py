from abc import ABC, abstractmethod

class Command(ABC):
	@abstractmethod
	def execute(self, *args):
		pass

	@abstractmethod
	def get_description(self):
		pass

#Addition
class AddCommand(Command):
	def __init__(self, strategy):
		self.strategy = strategy

	def execute(self, x, y):
		return self.strategy.calculate(x, y)

	def get_description(self):
		return "Add two numbers"

#Subtraction
class SubtractCommand(Command):
	def __init__(self, strategy):
		self.strategy = strategy

	def execute(self, x, y):
		return self.strategy.calculate(x,y)

	def get_description(self):
		return "Subtract two numbers"

#Multiplication
class MultiplyCommand(Command):
	def __init__(self, strategy):
		self.strategy = strategy

	def execute(self, x, y):
		return self.strategy.calculate(x,y)

	def get_description(self):
		return "Multiply two numbers"

#Division
class DivideCommand(Command):
	def __init__(self, strategy):
		self.strategy = strategy

	def execute(self, x, y):
		return self.strategy.calculate(x,y)

	def get_description(self):
		return "Divide two numbers"
