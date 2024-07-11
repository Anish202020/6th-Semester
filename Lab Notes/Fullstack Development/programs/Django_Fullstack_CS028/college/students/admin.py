from django.contrib import admin
from .models import Student, Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('courses',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
