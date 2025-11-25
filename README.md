# Setup
python -m venv venv
source venv/bin/activate
pip install Django==5.2.7

# Run
python manage.py runserver

# Test
curl -X POST http://127.0.0.1:8000/upload/ -F "file=@PATH_TO_YOUR_FILE"
