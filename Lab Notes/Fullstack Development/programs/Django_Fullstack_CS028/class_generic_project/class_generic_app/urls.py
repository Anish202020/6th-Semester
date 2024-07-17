from django.urls import path  
from .views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve, EmployeeUpdate, EmployeeDelete  
  
app_name = 'class_generic_app'  
urlpatterns = [  
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate'),  
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),  
    path('<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),  
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),  
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name = 'EmployeeDelete')  
  
]  