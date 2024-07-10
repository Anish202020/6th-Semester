# views.py
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
import os

def image_response_view(request):
    image_path = os.path.join(settings.MEDIA_ROOT, 'image.jpeg')
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')
    else:
        raise Http404("Image not found")
