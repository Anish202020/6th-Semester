from django import forms

class UserForm(forms.Form):
    USERNAME_MAX_LENGTH = 150  # This can be set according to your requirements

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    username = forms.CharField(max_length=USERNAME_MAX_LENGTH, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
