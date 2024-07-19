import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Student
def export_students_csv(request):
 response = HttpResponse(content_type='text/csv')
 response['Content-Disposition'] = 'attachment; filename="students.csv"'
 writer = csv.writer(response)
 writer.writerow(['First Name', 'Last Name', 'Enrollment Date'])
 students = Student.objects.all().values_list('first_name', 'last_name', 'enrollment_date')
 for student in students:
    writer.writerow(student)
    
 return response
def export_students_pdf(request):
 response = HttpResponse(content_type='application/pdf')
 response['Content-Disposition'] = 'attachment; filename="students.pdf"'
 p = canvas.Canvas(response)
 students = Student.objects.all()
 y = 800
 for student in students:
    p.drawString(100, y, f"{student.first_name} {student.last_name} - {student.enrollment_date}")
 y -= 20
 p.showPage()
 p.save()
 return response