import pandas as pd
import os

class HistoryManager:
	_instance = None

	def __new__(cls, history_file):
		if cls._instance == None:
			cls._instance = super().__new__(cls)
			cls._instance._init(history_file)
		return cls._instance

	def _init(self, history_file):
		self.history_file = history_file
		if os.path.exists(history_file):
			self.history = pd.read_csv(history_file)
		else:
			self.history = pd.DataFrame(columns=['Operation','x','y','answer'])

	def add_entry(self, operation, x, y, result):
		new_row = pd.DataFrame([{
			'Operation': operation,
			'x': x,
			'y': y,
			'answer':result
		}])
		self.history = pd.concat([self.history, new_row], ignore_index=True)

	def save_history(self):
		self.history.to_csv(self.history_file, index=False)

	def clear_history(self):
		self.history = pd.DataFrame(columns=['Operation', 'x', 'y', 'answer'])
		self.save_history()

	def get_history(self):
		return self.history
