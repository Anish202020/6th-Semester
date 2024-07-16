from .models import Employee  
from .forms import EmployeeForm  
from django.views.generic.edit import CreateView  
  
class EmployeeCreate(CreateView):  
    model = Employee  
  
    fields = '__all__'  