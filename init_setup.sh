echo [$(date)]: "START"

echo [$(date)]: "creating virtual environment 'env' with Python 3.8 version"

# Use python -m venv to create the virtual environment
python -m venv env

echo [$(date)]: "activating the environment"

# Activate the virtual environment for Bash
source ./env/Scripts/activate

echo [$(date)]: "installing the dev requirements"

# Install requirements using pip
pip install -r requirements_dev.txt

echo [$(date)]: "END"
