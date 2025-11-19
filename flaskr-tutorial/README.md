# Flaskr Tutorial

This is the Flask tutorial project - a basic blog application.

Tutorial: https://flask.palletsprojects.com/en/stable/tutorial/

## Project Layout

The project has the following structure:

```
flaskr-tutorial/
├── flaskr/             # Python package containing application code
│   └── __init__.py     # Application factory
├── tests/              # Test modules
├── instance/           # Instance folder (contains local data, not in version control)
├── pyproject.toml      # Project metadata and dependencies
└── MANIFEST.in         # Distribution file manifest
```

## Installation

Install the project in development mode:

```bash
cd flaskr-tutorial
pip install -e .
```

## Running the Application

```bash
flask --app flaskr run --debug
```

Visit http://127.0.0.1:5000/hello to see the test page.

## Development

The application is configured to use:
- Instance folder for local configuration and database
- SECRET_KEY='dev' (should be changed for production)
- SQLite database stored in the instance folder
