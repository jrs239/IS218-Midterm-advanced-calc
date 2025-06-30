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
	def execute(self, x, y):
		return x+y

	def get_description(self):
		return "Add two numbers"

#Subtraction
class SubtractCommand(Command):
	def execute(self, x, y):
		return x-y

	def get_description(self):
		return "Subtract two numbers"

#Multiplication
class MultiplyCommand(Command):
	def execute(self, x, y):
		return x*y

	def get_description(self):
		return "Multiply two numbers"

#Division
class DivideCommand(Command):
	def execute(self, x, y):
		if y == 0:
			raise ZeroDivisionError("Cannot divide by zero!")
		return x/y

	def get_description(self):
		return "Divide two numbers"
