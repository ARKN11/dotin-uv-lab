# Dotin UV Lab

A practical Python backend engineering learning project. The repository is being developed incrementally as part of a backend internship preparation roadmap.

At the current stage, it demonstrates Python package structure, domain-model validation, typed application code, Pydantic validation schemas, environment-based configuration, structured logging, and a reproducible `uv` workflow.

## Current scope

- Python 3.14+ and a `src/` package layout
- Domain entities with explicit runtime invariants
- Pydantic models for validated input data
- Pydantic Settings for environment-based configuration
- Type hints and strict static checking with mypy
- Module-level loggers and application-level logging configuration
- A small inventory module using `TypedDict`
- Git feature-branch and pull-request workflow

Automated tests are intentionally not part of this checkpoint yet; testing will be introduced as a separate learning block.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/ARKN11/dotin-uv-lab.git
cd dotin-uv-lab
```

Install the project and development dependencies:

```bash
uv sync
```

Create your local environment file:

**Git Bash**
```bash
cp .env.example .env
```

**PowerShell**
```powershell
Copy-Item .env.example .env
```

Edit `.env` and set a local database password. The current sample application only reports the configured database host and port; it does not connect to PostgreSQL yet.

Never commit `.env` or real credentials. The committed `.env.example` contains placeholders only.

## Run

```bash
uv run python -m dotin_uv_lab.main
```

Or use the installed project command:

```bash
uv run dotin-uv-lab
```

## Static type checking

```bash
uv run mypy
```

The mypy configuration is stored in `pyproject.toml` and checks the `dotin_uv_lab` package in strict mode.

## Project structure

```text
.
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
├── src/
│   └── dotin_uv_lab/
│       ├── __init__.py
│       ├── main.py
│       ├── settings.py
│       ├── inventory.py
│       ├── customers/
│       │   ├── __init__.py
│       │   └── models.py
│       ├── products/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   └── operations.py
│       ├── schemas/
│       │   ├── __init__.py
│       │   └── product.py
│       └── services/
│           ├── __init__.py
│           └── order_service.py
└── uv.lock
```

## Design notes

- `products/models.py` and `customers/models.py` contain ordinary Python domain entities. Their constructors enforce domain invariants; type annotations alone are not runtime validation.
- `schemas/` contains Pydantic models for data entering the application. These schemas are separate from the domain entities because they serve different responsibilities.
- `settings.py` contains application configuration loaded from environment variables. Secrets are represented with `SecretStr` and are not logged.
- `main.py` is the composition/entry-point module. Importing it does not start the application.
- Business logic belongs in domain models or service modules, not in package `__init__.py` files.

## Learning-project status

This is an educational repository, not a production-ready service. It does not yet expose HTTP endpoints, connect to PostgreSQL, or include automated tests. Those topics will be added in later roadmap stages.
