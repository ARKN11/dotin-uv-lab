# Dotin UV Lab

A Python practice project created during the Dotin Python Backend/FastAPI internship.

## Overview

This project demonstrates fundamental Python backend development practices, including:

- Python packages and modules
- Object-oriented programming basics
- Absolute and relative imports
- Separation of responsibilities
- Basic service-layer organization
- Python project and dependency management with `uv`

## Project Structure

```text
src/
└── dotin_uv_lab/
    ├── customers/
    │   ├── __init__.py
    │   └── models.py
    ├── products/
    │   ├── __init__.py
    │   ├── models.py
    │   └── operations.py
    ├── services/
    │   ├── __init__.py
    │   └── order_service.py
    ├── __init__.py
    └── main.py
```

## Requirements

- Python 3.14+
- uv

## Installation

Clone the repository:

```bash
git clone https://github.com/ARKN11/dotin-uv-lab.git
cd dotin-uv-lab
```

Install dependencies and synchronize the project environment:

```bash
uv sync
```

## Usage

Run the application from the project root:

```bash
uv run python -m dotin_uv_lab.main
```

The application creates sample customer and product objects and displays an order summary.

## Learning Purpose

This repository is a hands-on learning project. It will evolve as new Python backend development concepts are introduced throughout the internship.

## License

This project is for educational purposes.
