from django.forms import fields  
from .models import Employee  
from django import forms  
  
class EmployeeForm(forms.ModelForm):  
  
    class Meta:  
        # To specify the model to be used to create form  
        model = Employee  
        # It includes all the fields of model  
        fields = '__all__'  