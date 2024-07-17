from .models import Employee  
from .forms import EmployeeForm  
from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
  
class EmployeeCreate(CreateView):  
    model = Employee  
  
    fields = '__all__'  
class EmployeeRetrieve(ListView):  
    model = Employee  