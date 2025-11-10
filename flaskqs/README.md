## Flask Quickstart Assignment

# Setting up virtual environment
cd flaskqs
python -m venv venv
source venv/bin/activate

note this is for a Codespace or other Linux environment.

# Installing flask

pip install flask

# Create requirements.txt

(this allows you to easily reinstall)

pip freeze > requirements.txt

# Confirm flask is installed properly

flask --version

# Begin the Quickstart!

https://flask.palletsprojects.com/en/stable/quickstart/

# Notes

You should probably launch the venv from the terminal, and also run the program there,
so you don't have two competing virtual environments. (so don't click the dorito.)

Default command which runs app.py:

flask run

Alternative:

flask run --app minimal.py --debug

# From here

Build the QS!

