import os
from dotenv import load_dotenv
from .factory import CommandFactory
from .facade import HistoryFacade
from .logger import logger

def main():
    # Load environment variables from .env file if present
    load_dotenv()

    # Get history file path from env or use default
    history_file = os.getenv('HISTORY_FILE', 'calculator_history.csv')

    # Set up our factory and history facade
    factory = CommandFactory()
    history = HistoryFacade(history_file)

    logger.info("Calculator REPL started")

    print("Jorge Sanchez")
    print("IS218-450")
    print("Midterm Project")
    print("June 29th, 2025")
    print("\n---------------------------------------------------------\n")
    print("Advanced Calculator")
    print("Available Commands List \n ----- \n add \n subtract \n multiply \n divide \n -----")
# Print plugins too
    if factory.plugins:
        for plugin in factory.plugins:
            print(f" {plugin}")

    print(" -----")
    print("Type commands like \n (ex: add 2 3) \n (ex: divide 45 9) \n (ex: subtract 1007 911")
    print("\n---------------------------------------------------------\n")
    print("Type 'history' to see past calculations.")
    print("Type 'clear' to clear calculator history.")
    print("Type 'exit' to close the CLI")
    print("\n---------------------------------------------------------\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Calculator Shutdown")
            logger.info("exited calculator")
            break

        elif user_input.lower() == "history":
            print("\nYour past calculations:")
            print(history.show_history())
            logger.info("displayed history")

        elif user_input.lower() == "clear":
            history.clear_history()
            print("History Cleared")
            logger.info("Cleared history")

        else:
            try:
                logger.info(f"User command: {user_input}")
                # Split user input into parts
                parts = user_input.split()

                # First word is command name, rest are operands
                command_name = parts[0]
                args = [float(p) for p in parts[1:]]

                # Let the factory handle picking the right command
                command = factory.get_command(command_name)

                # Do the math!
                result = command.execute(*args)
                print(f"Result: {result}")
                logger.info(f"Calculation result: {result}")

                # Log it in history
                history.add_calculation(command_name.capitalize(), *args, result=result)
                logger.info(f"Added to history: {command_name.capitalize()} {args} = {result}")

            except Exception as e:
                print(f"Oops! Something went wrong: {e}")
                logger.error(f"Error processing input '{user_input}': {e}")

if __name__ == "__main__":
    main()
