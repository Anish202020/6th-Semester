from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.feedback_form, name='home'),
]
