# Django File Upload API

A simple Django REST API that accepts PDF, JPG, and PNG file uploads.

## Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install Django
pip install Django==5.2.7

# Start the development server
python manage.py runserver

# Upload a file
curl -X POST http://127.0.0.1:8000/upload/ -F "file=@/path/to/your/file.pdf"
```

