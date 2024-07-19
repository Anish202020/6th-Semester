from django.urls import path
from .views import export_students_csv, export_students_pdf
urlpatterns = [
 path('export/csv/', export_students_csv, name='export_students_csv'),
 path('export/pdf/', export_students_pdf, name='export_students_pdf'),
]