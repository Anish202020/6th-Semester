from django.shortcuts import render
from .models import Fruit, Student
def fruit_list(request):
    fruits = Fruit.objects.all()
    return render(request, 'list/fruit_list.html', {'fruits': fruits})
def student_list(request):
    students = Student.objects.all()
    return render(request, 'list/student_list.html', {'students': students})