from django.urls import path
from . import views
urlpatterns = [
 path('', views.course_list, name='course_list'),
 path('course/<int:course_id>/enroll/', views.enroll_student, name='enroll_student'),
 path('course/<int:course_id>/students/', views.enrolled_students, name='enrolled_students'),
]
