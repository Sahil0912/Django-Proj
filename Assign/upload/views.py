import os
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# status 400 ->bad request and 200->ok
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def upload_file(request):
    if request.method == 'OPTIONS':
        response = JsonResponse({'status': 'ok'})
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    if 'file' not in request.FILES:
        response = JsonResponse({
            'success': False,
            'error': 'No file provided'
        }, status=400)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    
    uploaded_file = request.FILES['file']
    
    allowed_extensions = ['.pdf', '.jpg', '.png']
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    
    if file_extension not in allowed_extensions:
        response = JsonResponse({
            'success': False,
            'error': f'Invalid file type. Allowed: PDF, JPG, PNG'
        }, status=400)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    
    job_key = str(uuid.uuid4())[:8]
    tmp_dir = os.path.join(settings.BASE_DIR, 'tmp')
    os.makedirs(tmp_dir, exist_ok=True)
    
    filename = f"{job_key}{file_extension}"    
    fs = FileSystemStorage(location=tmp_dir)
    saved_name = fs.save(filename, uploaded_file)
    file_path = os.path.join(tmp_dir, saved_name)
    response = JsonResponse({
        'success': True,
        'jobKey': job_key
    }, status=200)
    
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    
    return response
