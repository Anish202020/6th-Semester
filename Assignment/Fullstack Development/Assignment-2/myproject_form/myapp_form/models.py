from django.db import models

class UserData(models.Model):
    USERNAME_MAX_LENGTH = 150  # This can be set according to your requirements

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    username = models.CharField(max_length=USERNAME_MAX_LENGTH)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    text = models.TextField()

    def __str__(self):
        return self.username
