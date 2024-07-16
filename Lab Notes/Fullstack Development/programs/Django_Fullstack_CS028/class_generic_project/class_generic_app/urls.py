from django.urls import path  
from .views import EmployeeCreate  
  
urlpatterns = [  
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate')  
]  