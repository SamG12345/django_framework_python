python3.10 -m venv venv
source venv/bin/activate

python3 -m pip install

# Install requirements
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic
