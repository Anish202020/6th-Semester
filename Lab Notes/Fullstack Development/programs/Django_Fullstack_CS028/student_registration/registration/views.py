from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Enrollment
from django.http import HttpResponse
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'registration/course_list.html', {'courses': courses})
def enroll_student(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        student = get_object_or_404(Student, id=student_id)
        Enrollment.objects.create(student=student, course=course)
        return redirect('course_list')
    return render(request, 'registration/enroll_student.html', {'course': course, 'students': students})
def enrolled_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    return render(request, 'registration/enrolled_students.html', {'course': course, 'enrollments': enrollments})