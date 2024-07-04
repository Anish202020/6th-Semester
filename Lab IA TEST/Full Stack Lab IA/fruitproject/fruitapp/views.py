from django.shortcuts import render
from .models import Fruits, Students
def fruit_list(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruitapp/fruit_list.html', {'fruits': fruits})
def student_list(request):
    students = Students.objects.all()
    return render(request, 'fruitapp/student_list.html', {'students': students})