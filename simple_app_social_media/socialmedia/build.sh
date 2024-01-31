
# Upgrade pip
python3 -m pip install --upgrade pip

pip install python

# Install requirements
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic
