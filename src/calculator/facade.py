from .history import HistoryManager

class HistoryFacade:
    def __init__(self, history_file):
        self.manager = HistoryManager(history_file)

    def add_calculation(self, operation, *args, result):
        self.manager.add_entry(operation, *args, result=result)
        self.manager.save_history()

    def show_history(self):
        return self.manager.get_history()

    def clear_history(self):
        self.manager.clear_history()
