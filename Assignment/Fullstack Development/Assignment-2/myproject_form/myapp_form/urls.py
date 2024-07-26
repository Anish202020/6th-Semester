from django.urls import path
from .views import user_form_view, success_view

urlpatterns = [
    path('', user_form_view, name='user_form'),
    path('success/', success_view, name='success'),
]
