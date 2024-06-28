from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Course(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     def __str__(self):
        return self.name
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    enrolled_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('student', 'course')
        def __str__(self):
            return f'{self.student} enrolled in {self.course}'