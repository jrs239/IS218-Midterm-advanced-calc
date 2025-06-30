import os
from dotenv import load_dotenv
from .factory import CommandFactory
from .facade import HistoryFacade

def main():
    # Load environment variables from .env file if present
    load_dotenv()

    # Get history file path from env or use default
    history_file = os.getenv('HISTORY_FILE', 'calculator_history.csv')

    # Set up our factory and history facade
    factory = CommandFactory()
    history = HistoryFacade(history_file)

    print("Welcome to the Advanced Calculator!")
    print("Available commands: add, subtract, multiply, divide")
    print("Type commands like (ex: add 2 3)")
    print("Type 'history' to see past calculations.")
    print("Type 'clear' to clear calculator history.")
    print("Type 'exit' to close the CLI")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Goodbye! Have a good one!")
            break

        elif user_input.lower() == "history":
            print("\nYour past calculations:")
            print(history.show_history())

        elif user_input.lower() == "clear":
            history.clear_history()
            print("History wiped clean. Fresh start!")

        else:
            try:
                # Split user input into parts
                parts = user_input.split()

                # First word is command name, rest are operands
                command_name = parts[0]
                x = float(parts[1])
                y = float(parts[2])

                # Let the factory handle picking the right command
                command = factory.get_command(command_name)

                # Do the math!
                result = command.execute(x, y)
                print(f"Result: {result}")

                # Log it in history
                history.add_calculation(command_name.capitalize(), x, y, result)

            except Exception as e:
                print(f"Oops! Something went wrong: {e}")

if __name__ == "__main__":
    main()
