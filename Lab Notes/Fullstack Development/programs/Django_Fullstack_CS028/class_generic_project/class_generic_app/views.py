from django.shortcuts import redirect, render  
from django.urls import reverse, reverse_lazy  
from django.contrib import messages  
from .models import Employee  
from .forms import EmployeeForm  
from django.views.generic.edit import CreateView, DeleteView, UpdateView  
from django.views.generic.list import ListView  
from django.views.generic.detail import DetailView  
  
class EmployeeCreate(CreateView):  
    model = Employee  
  
    fields = '__all__'  
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')  
  
class EmployeeRetrieve(ListView):  
    model = Employee  
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')  
  
class EmployeeDetail(DetailView):  
    model = Employee  
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')  
  
class EmployeeUpdate(UpdateView):  
    model = Employee  
    template_name_suffix = '_update_form'  
    fields = '__all__'  
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')  
      
    # def get_success_url(self):  
          
      
      
class EmployeeDelete(DeleteView):  
    model = Employee  
    # here we can specify the URL   
    # to redirect after successful deletion  
    success_url = '/'  