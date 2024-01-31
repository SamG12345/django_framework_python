
# Upgrade pip
python3 -m pip install --upgrade pip

pip install python

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate


# Install requirements
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic
