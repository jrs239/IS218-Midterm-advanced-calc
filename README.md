# Advanced Calculator

Jorge Sanchez  
IS218-450  
Midterm Project  
June 29th, 2025

---

## About This Project
Hey everyone — Jorge here.

This project was honestly a bit tough to get through with work and my recent promotion. Balancing longer hours with school wasn’t easy. But it actually made me want to really dig in and learn how to do this *properly* instead of just hacking something together.

I wanted to see what real Python design patterns looked like, how to keep the project clean, and even set up automated testing. This repo is the result.

---

## How to Run
Clone the repo, install requirements, set up your `.env` (there’s an example file for that):

```bash
pip install -r requirements.txt

python -m src.calculator.main

-------------------------------------------------------------------------------------------------

## Features
- Interactive command-line interface
- Built-in operations
- Plugin system to add new commands dynamically
- History saved in CSV using pandas
- Logging to console or file
- Configurable via environment variables
- Fully tested with pytest
- GitHub Actions for automated tests on every push

## Design Patterns Used
I tried to really understand and implement these properly:

- Command Pattern — Each operation is a command object

- commands.py

- Strategy Pattern — Clean separation of calculation logic

- strategies.py

- Singleton Pattern — Single shared history manager

- history.py

- Facade Pattern — Simplifies interacting with pandas history

- facade.py

- Factory Pattern — Dynamically creates commands and loads plugins

## Exception Handling

- LBYL - plugin_loader.py
- EAFP - main.py

## Tests
All tests in tests/test_commands.py

Covers:

Add

Subtract

Multiply

Divide

Division by zero

Run them locally with:

```bash
PYTHONPATH=src pytest

