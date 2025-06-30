from abc import ABC, abstractmethod

class CalculationStrategy(ABC):
	@abstractmethod
	def calculate (self, x, y):
		pass

class AdditionStrategy(CalculationStrategy):
	def calculate(self, x, y):
		return x+y

class SubtractionStrategy(CalculationStrategy):
	def calculate(self, x, y):
		return x-y

class MultiplicationStrategy(CalculationStrategy):
	def calculate (self, x, y):
		return x*y

class DivisionStrategy(CalculationStrategy):
	def calculate (self, x, y):
		if y == 0:
			raise ZeroDivisionError("Cannot Divide by Zero")
		return x/y
