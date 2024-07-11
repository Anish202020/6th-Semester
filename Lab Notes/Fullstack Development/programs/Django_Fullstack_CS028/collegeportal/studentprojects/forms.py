from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['student_name', 'topic_chosen', 'languages_used', 'duration']
