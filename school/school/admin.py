from django.contrib import admin
from .models import Student, Teacher, Subject

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
