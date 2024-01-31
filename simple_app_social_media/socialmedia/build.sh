#!/bin/bash
# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
python3 -m pip install --upgrade pip

# Install SQLite development library
pip install django

# Install requirements
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic
