from django.urls import path
from .views import project_create_view, project_success_view
urlpatterns = [
    path('create/', project_create_view, name='project_create'),
    path('success/', project_success_view, name='project_success'),
]
