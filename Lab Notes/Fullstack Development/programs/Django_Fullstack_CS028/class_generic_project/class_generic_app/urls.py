from django.urls import path  
from .views import EmployeeCreate, EmployeeRetrieve  
  
urlpatterns = [  
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate'),  
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve')  
]  