# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('image/image/', views.image_response_view, name='image_response_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
