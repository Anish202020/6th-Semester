from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')

admin.site.register(Employee, EmployeeAdmin)
