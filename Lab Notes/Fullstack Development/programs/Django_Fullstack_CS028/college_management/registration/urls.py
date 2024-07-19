from django.urls import path
from . import views
urlpatterns = [
 path('register/', views.student_registration, name='student_registration'),
]
