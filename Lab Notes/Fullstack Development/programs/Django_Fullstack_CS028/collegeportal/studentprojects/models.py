from django.db import models

class Project(models.Model):
    student_name = models.CharField(max_length=100)
    topic_chosen = models.CharField(max_length=200)
    languages_used = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in weeks")

    def __str__(self):
        return self.student_name
