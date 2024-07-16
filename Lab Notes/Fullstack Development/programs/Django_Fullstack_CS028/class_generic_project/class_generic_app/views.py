from .models import Employee  
from .forms import EmployeeForm  
from django.views.generic.edit import CreateView  
from django.forms import fields  

class EmployeeCreate(CreateView):  
    model = Employee  
  
    fields = '_all_'