from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, default='')

class Project(models.Model):
    title = models.CharField(max_length=255, default='')

class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')
    courses = models.ManyToManyField(Course, related_name='students', blank=True)
    project = models.ManyToManyField(Project, related_name='students', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
