# CPS 310 Final Project Starter
## Recipe & Meal Planner

This repository contains the starter code for the CPS 310 final project.

The application currently supports:

- loading recipe data from JSON
- listing all recipes
- searching recipes by name
- filtering recipes by category
- viewing recipe details
- loading basic configuration from `config.json`
- loading meal plan data from meal_plan JSON
- adding but not preserving meal to plan
- view current meal plan
- sort and display recipes based on how long it takes to prep and cook them

This is intentionally a **starter project**, not a finished application.

## Setup

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

## Run Tests

### Windows

```powershell
python -m pytest -v
```

### macOS

```bash
python3 -m pytest -v
```

You are expected to make your own design decisions as you extend the project during the final project.
