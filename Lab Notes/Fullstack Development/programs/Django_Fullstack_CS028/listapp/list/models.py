from django.db import models
class Fruit(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
